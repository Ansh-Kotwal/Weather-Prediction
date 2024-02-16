from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dailyData_v1 import scrappingDailyData


class Scrapping: 
 def main(): 
    
  try:
   
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument(
   "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

   driver = webdriver.Chrome(chrome_options)
   driver.get("https://www.accuweather.com/")

   input_field = WebDriverWait(driver, 5).until( 
                EC.presence_of_element_located((By.CLASS_NAME, "search-input"))
            )


   input_field.send_keys("Mumbai")
   input_field.send_keys(Keys.RETURN)

   target_Location =  WebDriverWait(driver, 5).until( 
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]"))
            )
   

   link = target_Location.get_attribute('href')
   driver.get(link)

   element = driver.find_elements(By.CLASS_NAME, "subnav-item")
   
   
   dailydata = scrappingDailyData(driver ,element[2].text, element[2].get_attribute('href'))
    
   with open("output.json", "w") as outfile:
    json.dump(dailydata, outfile)
   
  # input("Enter to Quit")
   

  except:
   print("An exception occurred") 

# Class run
test_instance = Scrapping
con = test_instance.main()
    



