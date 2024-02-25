from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def scrappingHourlyData(driver , location ,url ):
    print("\n########################################################################################################################################\n")
    print("------ Scrapping Hourly data ------\n")
    
    dataList = [{"location":location}]
    
    for i in range(1,4):
        daily_url = url + f"?day={i}"
        
        data = {
            f"day{i}":fetchHourlyData(driver,daily_url , i)
        }
        
        dataList.append(data)
     
    print("\n------ Hourly Data Scrapping Completed ------") 
    # print("########################################################################################################################################")  
    return dataList


def fetchHourlyData(driver, url , day):
    driver.get(url)
    wait = WebDriverWait(driver, 5 )

    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.close_cross_big"))).click()
    
    time.sleep(2)
      

    cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hourly-card-top ')))
    
    for e in cards:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hourly-card-top')))
            e.click()
        

    
    time_tags = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'date')))
    temps = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'temp')))
    remarks = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'phrase')))
    precipitations = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'precip')))
    first_half_data = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'panel')))
        
        
    main_dict = []

    counter = 0

    for i in range(len(cards)):
        data_dict = {
            "time": time_tags[i].text,
            "temp": temps[i].text,
            "precipitation": precipitations[i].text,
            "remarks": remarks[i].text
        }

        data1 = first_half_data[counter].text.splitlines()
        counter += 1
        data2 = first_half_data[counter].text.splitlines()
        counter += 1

        for j in range(0, len(data1), 2):
            key, value = data1[j], data1[j + 1]
            data_dict[key] = value

        for j in range(0, len(data2), 2):
            key, value = data2[j], data2[j + 1]
            data_dict[key] = value

        main_dict.append(data_dict)

    print(f"-> Day {day} Hourly data collected ")
    return main_dict


    

