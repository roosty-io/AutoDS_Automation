from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# Set ChromeDriver path manually
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
GOOGLE_CHROME_PATH = "/usr/bin/google-chrome"

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_PATH
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

# Use the specified ChromeDriver path
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.google.com")
    print("✅ ChromeDriver is working!")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    driver.quit()

