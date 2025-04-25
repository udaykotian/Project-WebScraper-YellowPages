# Yellow Pages Business Scraper

This project scrapes business listings from Yellow Pages, extracting names, addresses, phone numbers, and websites. It uses Python with `selenium` to handle dynamically loaded content.

## How to Run

1. **Clone the repository**:

   git clone https://github.com/udaykotian/Project-WebScraper-YellowPages.git

2. **Install the required libraries**:

   pip install selenium

3. **Install ChromeDriver**:
- Download ChromeDriver matching your Chrome version from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
- Move it to `/usr/local/bin/` (or update the `CHROMEDRIVER_PATH` in the script).

4. **Run the scraper**:

   python yellowpages_scraper.py

5. **Check the output**:
- The scraped data will be saved in `yellowpages_businesses.csv`.

## Output Example

![Output Screenshot](output_screenshot.png)

## Notes

- This script runs in **non-headless mode** due to compatibility issues with ChromeDriver on macOS arm64 systems. To run in headless mode, you may need to adjust ChromeDriver settings or use a different system.
- Always check Yellow Pages' **terms of service** before scraping.

