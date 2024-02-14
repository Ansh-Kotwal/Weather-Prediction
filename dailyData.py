import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class

def getData( browser , url):
    
    try:
        wait = WebDriverWait(browser, 10 )
        print("inside getdata function")
        browser.get(url)


        open_daily_card = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "daily-forecast-card ")))
        link = open_daily_card.get_attribute('href')
        print(link)
        browser.get(link)
        print("opened daily data card")

        print("Scrapping data")
        temp_tag = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "temperature")))
        phrase_tag = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "phrase")))
        other_data = browser.find_elements(By.CLASS_NAME, "value")

        temp_text = temp_tag.text
        phrase = phrase_tag.text

        dataList = []

        for e in other_data:
            dataList.append(e.text)

        data = {
            "temp": temp_text,
            "wind": dataList[0],
            "wind_gust":dataList[1],
            "Probability of Precipitation":dataList[2],
            "Probability of Thunderstorms":dataList[3],
            "Precipitation": dataList[4],
            "cloud_cover": dataList[5],
            "remark": phrase
        }

        # Process and print the data
        json_data = json.dumps(data, indent=2)

        return json_data
    
    except Exception as e:
        print("Error Occored in getData function inside dailyData is :"+e)

