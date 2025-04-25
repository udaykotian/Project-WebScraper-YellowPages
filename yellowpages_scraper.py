"""
Yellow Pages Business Scraper

This script scrapes restaurant listings from Yellow Pages, extracting names, addresses, phone numbers, and websites.
It uses Selenium to handle dynamic content and saves the data to a CSV file.

Requirements:
- Install Selenium: `pip install selenium`
- Download ChromeDriver matching your Chrome version and place it in /usr/local/bin/
- Ensure Google Chrome is installed at /Applications/Google Chrome.app/
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Path to ChromeDriver
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
# Path to Chrome binary
CHROME_BINARY = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
URL = "https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New+York%2C+NY"

# Set up Chrome
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Headless mode disabled due to compatibility issues
options.binary_location = CHROME_BINARY
driver = webdriver.Chrome(service=service, options=options)

try:
    print("Navigating to URL...")
    driver.get(URL)
    print("Waiting for listings to load...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result"))
    )
    print("Listings found! Extracting data...")
    businesses = driver.find_elements(By.CLASS_NAME, "result")[:10]

    with open("yellowpages_businesses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Address", "Phone", "Website"])
        for business in businesses:
            # Extract name
            try:
                name = business.find_element(By.CLASS_NAME, "business-name").text.strip()
            except:
                name = "N/A"

            # Extract address
            try:
                address = business.find_element(By.CLASS_NAME, "street-address").text.strip()
            except:
                address = "N/A"

            # Extract phone
            try:
                phone = business.find_element(By.CLASS_NAME, "phones").text.strip()
            except:
                phone = "N/A"

            # Extract website
            try:
                website = business.find_element(By.CLASS_NAME, "track-visit-website").get_attribute("href")
            except:
                website = "N/A"

            writer.writerow([name, address, phone, website])
            print(f"Extracted: {name}, {address}, {phone}, {website}")
    print("Data saved to yellowpages_businesses.csv")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
    time.sleep(1)