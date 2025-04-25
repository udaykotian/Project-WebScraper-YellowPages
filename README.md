# Yellow Pages Business Scraper

This project scrapes business listings from Yellow Pages, extracting names, addresses, phone numbers, and websites. It uses Python with `selenium` to handle dynamically loaded content.

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A Python script that scrapes business listings from **Yellow Pages**, extracting *names*, *addresses*, *phone numbers*, and *websites*. It uses `selenium` to handle dynamically loaded content.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output Example](#output-example)
- [Notes](#notes)
- [License](#license)
- [Contributing](#contributing)

## Features

- Extracts business names, addresses, phone numbers, and websites from Yellow Pages.
- Saves data to a CSV file (`yellowpages_businesses.csv`).
- Handles dynamically loaded content using `selenium`.

## Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver compatible with your Chrome version

## Installation

1. **Clone the repository**:

    git clone https://github.com/udaykotian/Project-WebScraper-YellowPages.git
    cd Project-WebScraper-YellowPages

2. **Install the required libraries**:

    pip install selenium

3. **Install ChromeDriver**:
    - Download ChromeDriver matching your Chrome version from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
    - Move it to `/usr/local/bin/` (or update the `CHROMEDRIVER_PATH` in the script).

## Usage

1. **Run the scraper**:

    python yellowpages_scraper.py

2. **Check the output**:
    - The scraped data will be saved in `yellowpages_businesses.csv`.

## Output Example

Below is a sample of the data saved in `yellowpages_businesses.csv`:

![Output Screenshot](output_screenshot.png)

## Notes

- ⚠️ This script runs in **non-headless mode** due to compatibility issues with ChromeDriver on macOS arm64 systems. To run in headless mode, you may need to adjust ChromeDriver settings or use a different system.
- 📜 Always check Yellow Pages' **terms of service** before scraping.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.
