# AccuWeather Data Scraper

## Overview

This Python program scrapes weather data from the AccuWeather website using Selenium. It consists of four main files:

1. `automation.py`: Contains functions for automating the navigation to the AccuWeather website and fetching the daily URL.
2. `ConstructData.py`: Defines functions for constructing and combining data from consecutive days.
3. `dailyData.py`: Implements the web scraping logic to extract data from the AccuWeather website.
4. `main.py`: The main program that orchestrates the entire process, calling functions from the other files.

## Prerequisites

Make sure you have the following dependencies installed:

- Python
- Selenium
  ```bash
  pip install selenium
  ```

- Webdriver for your preferred browser (e.g., ChromeDriver)

## Usage

1. Run `main.py` to initiate the data scraping process.
   ```bash
   python main.py
   ```

## File Descriptions

### 1. `automation.py`

- `getLink()`: Opens the AccuWeather website and fetches the link of the daily URL.

### 2. `ConstructData.py`

- `getJson()`: Opens the daily URL of 10 consecutive days and calls `getData()` in `dailyData.py`. Combines data from consecutive days and returns it to `main.py`.

### 3. `dailyData.py`

- `getData()`: Scrapes data from the AccuWeather website for a single day.

### 4. `main.py`

- Main program that orchestrates the entire process, calling functions from other files.

## Notes

- Ensure that the webdriver is correctly configured and the browser is installed.
- Customize the scraping logic in `dailyData.py` based on the website structure and requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

# Happy Scraping
