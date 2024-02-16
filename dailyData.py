import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class

def getData(browser , url):
    print("inside getData function")
    
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10 )
        print("Scrapping data")
        
        date_day_tag = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div[7]/div[1]/div[1]/div[1]/div")))
        temp_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "temperature")))
        phrase_tag =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "phrase")))
        day_night_tag = browser.find_elements(By.CLASS_NAME, "title")
        other_data = browser.find_elements(By.CLASS_NAME, "value")

        date = date_day_tag[0].text
        date = date.split(",")

        if len(day_night_tag) == 6:  

            data = {
                "date":date[1],
                "day":date[0],
                    "day_time":{
                            "available":1,
                            "temp": temp_tag[0].text,
                            "max_uv_index":other_data[0].text,
                            "wind": other_data[1].text,
                            "wind_gust":other_data[2].text,
                            "probability_of_precipitation":other_data[3].text,
                            "probability_of_thunderstorms":other_data[4].text,
                            "Precipitation": other_data[5].text,
                            "cloud_cover": other_data[6].text,
                            "remark": phrase_tag[0].text,
                            },
                    "night_time":{
                            "temp": temp_tag[1].text,
                            "wind": other_data[7].text,
                            "wind_gust":other_data[8].text,
                            "probability_of_precipitation":other_data[9].text,
                            "probability_of_thunderstorms":other_data[10].text,
                            "Precipitation": other_data[11].text,
                            "cloud_cover": other_data[12].text,
                            "remark": phrase_tag[1].text,
                            }
                    }
        else:
           data = {
               "date":date[1],
                "day":date[0],
                "day_time":{
                    "available":0
                    },
                "night_time":{
                        "temp": temp_tag[0].text,
                        "wind": other_data[0].text,
                        "wind_gust":other_data[1].text,
                        "Probability of Precipitation":other_data[2].text,
                        "Probability of Thunderstorms":other_data[3].text,
                        "Precipitation": other_data[4].text,
                        "cloud_cover": other_data[5].text,
                        "remark": phrase_tag[0].text
                        }
                }

        print("End of  getData function")
        return data
    
    except Exception as e:
        print("Error Occored in getData function inside dailyData is :"+e)
        
        
        
def getJson(browser , daily_url , location):
    
    print("inside getJson function")

    index = daily_url.find("city=")
    daily_url = daily_url[:index]

    jsonData =  dict({"location":location})
    for i in range(1,10):
        main_card_url = daily_url+"day="+str(i)
        data = {
            "day "+str(i) : getData(browser,main_card_url)
        }
        jsonData.update(data)
        json_data=json.dumps(jsonData, indent=2)


    return json_data

