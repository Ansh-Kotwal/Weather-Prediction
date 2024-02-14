# import time
from dailyData import getData
from automation import Automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class



class Main:
    automation = Automation()
    
    browser = webdriver.Chrome()
    browser.get("https://www.accuweather.com/")
    
    daily_url = automation.getURL(browser , "Haldwani")
    print(daily_url)
    print("goint to getData")
    
    data = getData(browser , daily_url)
    
    browser.close()