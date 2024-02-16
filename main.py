from dailyData import getJson
from automation import getURL
from selenium import webdriver

def scrapData(location):
    
    browser = webdriver.Chrome()
    browser.get("https://www.accuweather.com/")
    daily_url = getURL(browser , location)
    print(daily_url)
    
    jsonData = getJson(browser, daily_url , location)
    
    print(jsonData)
    
    browser.close()
    
json_data = scrapData("Haldwani")
print(json_data)