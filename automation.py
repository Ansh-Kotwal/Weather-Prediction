import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class


class Automation:
    
    def getURL(self,browser,location):
        try:
            
            wait = WebDriverWait(browser, 10 )

            searchbox = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input")))
            time.sleep(1)
            searchbox.send_keys(location)
            searchbox.send_keys(Keys.ENTER)

            regionTag= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]')))
            
            region_link = regionTag.get_attribute('href')
            browser.get(region_link)
            
            
            url = browser.current_url
            daily_url = url.replace("weather-forecast","daily-weather-forecast")
            
            return daily_url
   
        except Exception as e:
            print("Error is :"+ str(e))


            
            
   
    
            

            
        
            
    
    