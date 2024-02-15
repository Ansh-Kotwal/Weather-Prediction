import json
from dailyData import getData
from automation import Automation
from ConstructData import getJson;
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class



class Main:
    automation = Automation()
    
    browser = webdriver.Chrome()
    browser.get("https://www.accuweather.com/")
    
    daily_url = automation.getURL(browser , "Dehradun")
    print(daily_url)
    
    jsonData = getJson(browser, daily_url)
    
    print(jsonData)
    
    json_data = json.dumps(jsonData)
    print(json_data)
    
    with open("output.json", "w") as outfile:
        json.dump(jsonData, outfile)
        
        
    browser.close()