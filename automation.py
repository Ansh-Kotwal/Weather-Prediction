import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class


class Automation:
    
    def getURL(self,location):
        try:

            browser = webdriver.Chrome()
            browser.get("https://www.accuweather.com/")

            wait = WebDriverWait(browser, 10 )

            searchbox = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input")))
            time.sleep(1)
            searchbox.send_keys(location)
            searchbox.send_keys(Keys.ENTER)


            regionSelector = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]')))
            # regionSelector.send_keys(Keys.CONTROL,Keys.F12)
            regionLink = regionSelector.get_attribute('href')
            browser.get(regionLink)
            
            element = browser.find_elements(By.CLASS_NAME, "subnav-item")

            for e in element:
                print(e.get_attribute('href'))
            
            
            input("Enter")
            url = browser.current_url
         
            # today_url = url.replace("weather-forecast","current-weather")
            daily_url = url.replace("weather-forecast","daily-weather-forecast")
            # hourly_url = url.replace("weather-forecast","hourly-weather-forecast")
            
            print(daily_url)
            
            input("press Enter")
            return daily_url
            
            
            
            
        
        except Exception as e:
            print("Error is :"+ str(e))

        finally:
            browser.close()
            
        
            
    
    