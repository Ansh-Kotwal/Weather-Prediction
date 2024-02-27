from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scrappingDailyData(driver , url):
 
 print("\n########################################################################################################################################\n")
 print("------ Scrapping Daily Data ------\n")
 
 daily_Data = []

 for day in range (1 , 45):
   perDayData(driver , f"{url}?day={day}" , day , daily_Data)
   print(f"-> Day {day} data collected")

 print("\n------ Daily Data Scrapping Completed ------")
#  print("########################################################################################################################################")
 return daily_Data
        
def perDayData(driver , dayUrl , day , daily_Data):
   driver.get(dayUrl)
   wait = WebDriverWait(driver, 5 )

   temp_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "temperature")))
   phrase_tag =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "phrase")))
   panels = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "panels")))

   day_panel = panels[0].text.splitlines() 
   night_panel = panels[(len(panels)-1)].text.splitlines()  

   per_Day_Data = {
                     "day":{
                            "Available" : 0,
                            "Temperature": None,
                            "Max UV Index": None,
                            "Wind": None,
                            "Wind Gusts": None,
                            "Probability of Precipitation": None,
                            "Probability of Thunderstorms": None,
                            "Precipitation": None,
                            "Rain": 0, 
                            "Hours of Precipitation":0, 
                            "Hours of Rain" : 0,
                            "Cloud Cover": None,
                            "Remark": None
                           },
                    "night":{                
                            "Temperature": temp_tag[(len(temp_tag)-1)].text,
                            "Wind": 0,
                            "Wind Gusts" : 0,
                            "Probability of Precipitation":  0,
                            "Probability of Thunderstorms": 0,
                            "Precipitation":  0,
                            "Rain": 0 , 
                            "Hours of Precipitation":0, 
                            "Hours of Rain" : 0,
                            "Cloud Cover":  0,
                            "Remark": phrase_tag[(len(phrase_tag)-1)].text,
                            }
                    }
   
   
    
   if(len(panels) == 2): 
    per_Day_Data["day"]["Available"] = 1
    per_Day_Data["day"]["Temperature"] = temp_tag[0].text
    per_Day_Data["day"]["Remark"] = phrase_tag[0].text

    for i in range (0 , len(day_panel) , 2):
       per_Day_Data["day"][f"{day_panel[i]}"]=day_panel[i+1]
   else:
    print("No day data available")   


   for i in range (0 , len(night_panel) , 2):  
       per_Day_Data["night"][f"{night_panel[i]}"]= night_panel[i+1]
            
   dataAppend(day , per_Day_Data , daily_Data)
   
def dataAppend(day , per_Day_Data , daily_Data):
  
  per_Day_Data = {
            f"day {day}" : per_Day_Data
        }
     
  daily_Data.append(per_Day_Data)    
       
def flattenDailyDataJson(json_data):
    flattened_data = []
    for record in json_data:
        for key, value in record.items():
            day_number = key
            day = value['day']
            night = value['night']
            flattened_record = {
                'Days': day_number.capitalize(),
                'Day Temperature': day['Temperature'],
                'Max UV Index': day['Max UV Index'],
                'Day Wind': day['Wind'],
                'Day Wind Gust': day['Wind Gusts'],
                'Day Probability of Precipitation': day['Probability of Precipitation'],
                'Day Probability of Thunderstorms': day['Probability of Thunderstorms'],
                'Day Precipitation': day['Precipitation'],
                'Day Rain': day['Rain'],
                'Day Hours of Precipitation': day['Hours of Precipitation'],
                'Day Hours of Rain': day['Hours of Rain'],
                'Day Cloud Cover': day['Cloud Cover'],
                'Day Remark': day['Remark'],
                'Night Temperature': night['Temperature'],
                'Night Wind': night['Wind'],
                'Night Wind Gust': night['Wind Gusts'],
                'Night Probability of Precipitation': night['Probability of Precipitation'],
                'Night Probability of Thunderstorms': night['Probability of Thunderstorms'],
                'Night Precipitation': night['Precipitation'],
                'Night Rain': night['Rain'],
                'Night Hours of Precipitation': night['Hours of Precipitation'],
                'Night Hours of Rain': night['Precipitation'],
                'Night Cloud Cover': night['Hours of Rain'],
                'Night Remark': night['Remark']
            }
            flattened_data.append(flattened_record)
    return flattened_data 
    
  