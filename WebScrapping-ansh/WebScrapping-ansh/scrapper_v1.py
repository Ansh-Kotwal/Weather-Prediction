from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dailyData_v1 import scrappingDailyData
from jsonOutput import jsonOutputFile
from excelOutput import json_to_excel
from hourlyData import getHourlyData
import json


class Scrapping: 
 def scrappingData(driver , location): 
    
  try:
   

   wait = WebDriverWait(driver , 5 )

   input_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-input")))
   input_field.send_keys(location)
   input_field.send_keys(Keys.RETURN)

   target_Location =  wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]")))
   link = target_Location.get_attribute('href')
   driver.get(link)

   element = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'subnav-item')))
   # element = driver.find_elements(By.CLASS_NAME, "subnav-item")?
   heading = element[2].text  # DAILY
   
   daily_href = element[2].get_attribute('href')
   hourly_href = element[1].get_attribute('href')
   
   
   daily_data = scrappingDailyData(driver , heading, daily_href) 
   jsonOutputFile(location ,"daily", daily_data) 
   
   
   print("Getting daily datas")
   hourly_data = getHourlyData(driver, location  ,hourly_href)
   jsonOutputFile(location , "hourly", hourly_data) 
   

   f = open(f"{location.capitalize()}WeatherdailyInfo.json")
   json_data = json.load(f)
   json_to_excel(json_data, f"{location.capitalize()}WeatherInfo.xlsx")

   

  except Exception as e:
   print(e) 



# Class run
#test_instance = Scrapping
#con = test_instance.main()
    



