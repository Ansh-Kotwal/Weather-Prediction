from dailyData import getJson
from automation import getURL
from selenium import webdriver
import json

def scrapData(location):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

    browser = webdriver.Chrome(chrome_options)
    browser.get("https://www.accuweather.com/")
    daily_url = getURL(browser , location)
    print(daily_url)
    
    jsonData = getJson(browser, daily_url , location)
    with open(f"{location.capitalize()}WeatherInfo.json", "w") as outfile:
        json.dump(jsonData, outfile)
    
    print(jsonData)
    
    browser.close()
    
json_data = scrapData("New York")
print(json_data)