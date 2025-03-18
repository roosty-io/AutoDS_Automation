from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")

service = Service("PATH_TO_CHROMEDRIVER")  # Replace with your actual path to ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# AutoDS Login Credentials
AUTODS_EMAIL = "your_email@example.com"  # Replace with your AutoDS login email
AUTODS_PASSWORD = "your_password"  # Replace with your AutoDS password

try:
    # Step 1: Navigate to AutoDS login page
    driver.get("https://autods.com/login")
    time.sleep(3)  # Wait for page to load

    # Step 2: Enter email and password
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    email_input.send_keys(AUTODS_EMAIL)
    password_input.send_keys(AUTODS_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login

    # Step 3: Navigate to the order reports page
    driver.get("https://autods.com/orders")
    time.sleep(5)

    # Step 4: Click on the "Export Report" button
    export_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Export Report')]")
    export_button.click()
    time.sleep(3)

    # Step 5: Wait for the CSV download link to appear & fetch it
    csv_link = driver.find_element(By.XPATH, "//a[contains(@href, '.csv')]").get_attribute("href")

    if csv_link:
        print(f"CSV Download Link: {csv_link}")

        # Download the file
        os.system(f"wget -O AutoDS_Report.csv {csv_link}")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()  # Close the browser
