from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class

def getData( browser , url):
    print("inside getData function")
    
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10 )
        print("opened daily data card")
        print("Scrapping data")
        
        date_day_tag = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div[7]/div[1]/div[1]/div[1]/div")))
        temp_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "temperature")))
        phrase_tag =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "phrase")))
        day_night_tag = browser.find_elements(By.CLASS_NAME, "title")
        other_data = browser.find_elements(By.CLASS_NAME, "value")

        date = date_day_tag[0].text
        date = date.split(",")

        dataList = []
        for e in other_data:
            dataList.append(e.text)

        print(len(day_night_tag))

        if len(day_night_tag) == 6:  

            data = {
                "date":date[1],
                "day":date[0],
                    "day_time":{
                            "temp": temp_tag[0].text,
                            "max_uv_index":dataList[0],
                            "wind": dataList[1],
                            "wind_gust":dataList[2],
                            "probability_of_precipitation":dataList[3],
                            "probability_of_thunderstorms":dataList[4],
                            "Precipitation": dataList[5],
                            "cloud_cover": dataList[6],
                            "remark": phrase_tag[0].text,
                            },
                    "night_time":{
                            "temp": temp_tag[1].text,
                            "wind": dataList[7],
                            "wind_gust":dataList[8],
                            "probability_of_precipitation":dataList[9],
                            "probability_of_thunderstorms":dataList[10],
                            "Precipitation": dataList[11],
                            "cloud_cover": dataList[12],
                            "remark": phrase_tag[1].text,
                            }
                    }
        else:
           data = {
               "date":date[1],
                "day":date[0],
                "day_time":"data not available",
                "night_time":{
                        "temp": temp_tag[0].text,
                        "wind": dataList[0],
                        "wind_gust":dataList[1],
                        "Probability of Precipitation":dataList[2],
                        "Probability of Thunderstorms":dataList[3],
                        "Precipitation": dataList[4],
                        "cloud_cover": dataList[5],
                        "remark": phrase_tag[0].text
                        }
                }

        print("End of  getData function")
        return data
    
    except Exception as e:
        print("Error Occored in getData function inside dailyData is :"+e)

