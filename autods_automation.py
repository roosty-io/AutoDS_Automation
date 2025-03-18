from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Automatically install the correct ChromeDriver version
chromedriver_autoinstaller.install()

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.google.com")
    print("✅ ChromeDriver is working!")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    driver.quit()
