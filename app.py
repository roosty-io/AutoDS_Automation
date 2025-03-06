from flask import Flask, request, jsonify

app = Flask(__name__)

# Your eBay Verification Token
EBAY_VERIFICATION_TOKEN = "TYCXkCynpUtEipOOfG3EJcR1U0QarK4rAwSp2AL2URM"

@app.route("/", methods=["GET"])
def home():
    """Root endpoint to check if the webhook is running."""
    return jsonify({"message": "Webhook is running"}), 200

@app.route("/ebay-webhook", methods=["POST", "GET"])
def ebay_webhook():
    """Handles eBay Marketplace Account Deletion notifications."""
    
    if request.method == "GET":
        # eBay's verification challenge
        challenge = request.args.get("challenge")
        verification_token = request.args.get("verification_token")

        # Validate verification token
        if verification_token == EBAY_VERIFICATION_TOKEN:
            return jsonify({"challengeResponse": challenge}), 200
        else:
            return jsonify({"error": "Invalid verification token"}), 403

    elif request.method == "POST":
        # Handle actual marketplace account deletion notification
        try:
            data = request.json
            print("🔔 Received eBay notification:", data)  # Log it for debugging

            return jsonify({"message": "Notification received successfully"}), 200
        except Exception as e:
            print(f"❌ Error processing notification: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

