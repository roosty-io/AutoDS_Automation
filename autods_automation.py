from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import os

# Install ChromeDriver automatically
chromedriver_autoinstaller.install()

# Define Chrome binary path
GOOGLE_CHROME_PATH = "/usr/local/bin/google-chrome"

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_PATH
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.google.com")
    print("✅ Chrome is working!")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    driver.quit()
