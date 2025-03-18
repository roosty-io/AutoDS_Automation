import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Debugging logs
logging.basicConfig(level=logging.DEBUG)
print("✅ Debug Mode: Script is running...")

try:
    # Install ChromeDriver automatically
    chromedriver_autoinstaller.install()

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.google.com")
    print("✅ ChromeDriver is working!")
    driver.quit()

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
