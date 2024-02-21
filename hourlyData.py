from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def fetchHourlyData(driver, url):
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hourly-card-top ')))

    main_dict = []

    for e in cards:
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

    time_tags = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'date')))
    temps = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'temp')))
    remarks = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'phrase')))
    precipitations = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'precip')))
    first_half_data = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'panel')))

    for i in range(len(cards)):
        data_dict = {
            "time": time_tags[i].text,
            "temp": temps[i].text,
            "precipitation": precipitations[i].text,
            "remarks": remarks[i].text
        }

        data1 = first_half_data[2 * i].text.splitlines()
        data2 = first_half_data[2 * i + 1].text.splitlines()

        for j in range(0, len(data1), 2):
            key, value = data1[j], data1[j + 1]
            data_dict[key] = value

        for j in range(0, len(data2), 2):
            key, value = data2[j], data2[j + 1]
            data_dict[key] = value

        main_dict.append(data_dict)

    print("collected")
    return main_dict

def getHourlyData(driver, location, url):
    print("Getting Hourly data")

    dataList = [{"location": location}]

    for i in range(1, 4):
        daily_url = url + f"?day={i}"

        data = {
            f"day{i}": fetchHourlyData(driver, daily_url)
        }

        dataList.append(data)

    return dataList