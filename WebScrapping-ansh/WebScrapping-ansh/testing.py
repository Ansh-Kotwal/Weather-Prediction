from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from jsonOutput import jsonOutputFile
import time
from selenium import webdriver


def fetchHourlyData(driver , url ):
    print("Hello")
    driver.get(url)
    

    time.sleep(2)
    
    wait = WebDriverWait(driver, 5)
    cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hourly-card-top ')))
    

    # time.sleep(2)
    # wait.until(lambda _: all(e.is_enabled() for e in cards))
    
    for e in cards:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hourly-card-top')))
            e.click()

        
        
        
    time_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'date')))
    temp = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'temp')))
    remark = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'phrase')))
    precipitation = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'precip')))
    first_half_data = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'panel')))
        
        
        
    main_dict = []
    
    counter = 0
    
    for i in range(0, len(cards)):
        
        data_dict = {
            "time":time_tag[i].text,
            "temp":temp[i].text,
            "precipitation":precipitation[i].text,
            "remarks":remark[i].text
        }
        
        data1 = first_half_data[counter].text.splitlines()
        counter+=1
        data2 = first_half_data[counter].text.splitlines()      
        counter+=1
        
        j = 0
        while j<len(data1):
            key = data1[j]
            j+=1
            value = data1[j]
            j+=1
            
            pair = {key:value}
            data_dict.update(pair)
        
        j=0
        while j<len(data2):
            key = data2[j]
            j+=1
            value = data2[j]
            j+=1
            
            pair = {key:value}
            data_dict.update(pair)
          
          
        main_dict.append(data_dict)
       
        
    return main_dict
        

    
def getHourlyData(driver , location ,url ):
    
    dataList = [{"location":location}]
    
    for i in range(1,4):
        daily_url = url + f"?day={i}"
        
        data = {
            f"day{i}":fetchHourlyData(driver,daily_url)
        }
        
        dataList.append(data)
        
    
    return dataList
