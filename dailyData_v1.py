from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json


def scrappingDailyData(driver , heading , url):
 print(heading + " = " + url)
 
 jsonData = []

 for day in range (1 , 45):
   jsondata(driver , f"{url}?day={day}" , day , jsonData)


 json_data = json.dumps(jsonData)
   
 with open("output.json", "w") as outfile:
    json.dump(jsonData, outfile)
        
 print("JSON FILE CREATED")


def jsondata(driver , dayUrl , day , jsonData):
   #print(dayUrl)
   driver.get(dayUrl)
   wait = WebDriverWait(driver, 10 )

   temp_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "temperature")))
   phrase_tag =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "phrase")))
   day_night_tag = driver.find_elements(By.CLASS_NAME, "title")
   other_data = driver.find_elements(By.CLASS_NAME, "value")


   #print(len(day_night_tag))

   if len(day_night_tag) == 6:  

            data = {
                    "day":{
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
                    "night":{
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
            temp_text = temp_tag.text
            phrase = phrase_tag.text

            data = {
                    "day":"data not available",
                    "night":{
                            "temp": temp_text,
                            "wind": other_data[0].text,
                            "wind_gust":other_data[1].text,
                            "Probability of Precipitation":other_data[2].text,
                            "Probability of Thunderstorms":other_data[3],
                            "Precipitation": other_data[4].text,
                            "cloud_cover": other_data[5].text,
                            "remark": phrase
                            }
                    }

   #print(" End of  getData function ")
   jsonformat(day , data , jsonData)
   

def jsonformat(day , data , jsonData):
  
  data = {
            f"day{day}" : data
        }   
  jsonData.append(data)    
       
 
    
  