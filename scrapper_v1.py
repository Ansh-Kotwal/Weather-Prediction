from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dailyData_v1 import scrappingDailyData , flattenDailyDataJson
from jsonOutput import jsonOutputFile
from excelOutput import json_to_excel
from historicalData import *
from hourlyData import scrappingHourlyData
from airQualityData import scrappingAQIData



class Scrapping: 
 def scrappingData(location): 
    
  try:
   
#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument("--headless")
#    chrome_options.add_argument(
#    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
#    chrome_options.add_argument('--blink-settings=imagesEnabled=false')

#    driver = webdriver.Chrome(chrome_options)

   firefox_options = webdriver.FirefoxOptions()
   firefox_options.add_argument("--headless")
   firefox_options.add_argument('--blink-settings=imagesEnabled=false')
   driver = webdriver.Firefox(firefox_options)


   driver.get("https://www.accuweather.com/")

   input_field = WebDriverWait(driver, 5).until( 
                EC.presence_of_element_located((By.CLASS_NAME, "search-input"))
            )


   input_field.send_keys(location)
   input_field.send_keys(Keys.RETURN)

   target_Location =  WebDriverWait(driver, 5).until( 
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]"))
            )
   

   link = target_Location.get_attribute('href')
   driver.get(link)

   element = driver.find_elements(By.CLASS_NAME, "subnav-item")

   hourly_data = element[1].get_attribute('href')
   daily_url = element[2].get_attribute('href')
   aqi_url = element[6].get_attribute('href')
   
   ####################################################################
   
   hourly_data = scrappingHourlyData(driver , location , hourly_data)

   jsonOutputFile(location , hourly_data , "HourlyData" )

   ####################################################################

   daily_data = scrappingDailyData(driver , daily_url)

   jsonOutputFile(location , daily_data , "DailyData")

   flatten_json_data = flattenDailyDataJson(daily_data)

   json_to_excel(flatten_json_data, f"{location.capitalize()}DailyData.xlsx")

   ####################################################################
   
   aqi_data = scrappingAQIData(driver , aqi_url )
   
   jsonOutputFile(location , aqi_data , "AQIData" )
     
   ####################################################################
   
   historical_data = scrappingHistoricalData(location)
   
   json_to_excel(historical_data , f"{location.capitalize()}HistoricalData.xlsx")

   ####################################################################

  except Exception as e:
   print(e) 



# Class run
#test_instance = Scrapping
#con = test_instance.main()
    



