
# Weather Prediction

The Weather Prediction project aims to gather, process, and analyze weather and air quality data from reliable online sources. By utilizing web scraping techniques, data processing, and storage, this project allows users to access and analyze weather patterns and air quality conditions for specific locations. The application can output data in both JSON and Excel formats, making it flexible for further analysis or integration with other applications.

# Overview

The Weather Prediction tool leverages Python to gather data about the weather and air quality in real-time. The data is scraped from trusted online sources and is processed into structured formats for easy consumption. This tool supports both hourly and daily weather data, along with air quality readings, which users can download for analysis.

Key features of the project include:
- Automated Web Scraping: Collects weather and air quality data from reliable sources automatically.
- Data Processing: Processes and structures raw data to provide meaningful insights.
- Multiple Output Formats: Users can export the data to JSON and Excel formats.
- Real-Time Data: Get the most up-to-date weather information for accurate predictions.

## Features

- **Web Scraping**: Automatically fetches real-time weather and air quality data from trusted sources. This includes temperature, humidity, air quality index (AQI), and more.
- **Data Processing**:  Cleans, structures, and organizes the scraped data into easily understandable formats.
- **Multiple Output Formats**: The processed data is exported in both JSON and Excel formats for ease of use in data analysis.
- **Historical Data Handling**: Allows users to analyze past weather trends and air quality information.
- **Interactive Data Exploration**: Facilitates visualizations and deeper insights based on the data collected.


## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Ansh-Kotwal/Weather-Prediction.git
   cd Weather-Prediction
   ```

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to start the data collection and processing pipeline:


```bash
python main.py
```


The script will execute the following modules:

- `scrapper_v1.py`: Scrapes current weather and air quality data.
- `dailyData_v1.py`: Processes daily weather data.
- `hourlyData.py`: Processes hourly weather data.
- `airQualityData.py`: Processes air quality data.
- `historicalData.py`: Handles historical weather data.
- `jsonOutput.py`: Exports data to JSON format.
- `excelOutput.py`: Exports data to Excel format.

## Project Structure


```plaintext
Weather-Prediction/
├── Excel/
├── Flow/
├── Json/
├── __pycache__/
├── airQualityData.py
├── dailyData_v1.py
├── excelOutput.py
├── historicalData.py
├── hourlyData.py
├── jsonOutput.py
├── main.py
├── requirements.txt
├── scrapper_v1.py
└── README.md
```


## Author

[Ansh Kotwal](https://github.com/Ansh-Kotwal)

---
