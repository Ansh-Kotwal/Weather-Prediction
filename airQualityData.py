from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from jsonOutput import jsonOutputFile




firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options)

def scrappingAQIData(driver , url ):
  driver.get(url)
  wait = WebDriverWait(driver, 5 )
  print("\n########################################################################################################################################\n") 
  print("------ Scrapping AQI Data ------\n")

  view_more = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more")))
  driver.execute_script("arguments[0].click();", view_more)


  day = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "day-of-week")))
  date = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "date")))
  daily_card = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content-wrapper")))
  pollutant_card = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "air-quality-pollutant")))


  pollutants_data = []
  for e in pollutant_card:
   temp = list(e.text.splitlines())
   x = len(temp)
   pollutants = {
            temp[0] : {
            "condition" : temp[1]  ,
           "pollutant_index": temp[x-2],
            "pollutant-concentration" : temp[x-1],
            "statement" : temp[2]
           } 
         }
   pollutants_data.append(pollutants)

  daily_data =[]
  i = 1
  for e in range(1 , len(daily_card)):
   temp = list(daily_card[e].text.splitlines())
   daily_aqi = {
            "day" : day[i].text ,
            "date" : date[i].text ,
            "aqi_value" : temp[0] ,
            "condition" : temp[2] ,
            "statement" : temp [3]

         }
   i=i+1
   daily_data.append(daily_aqi)

   data = {
     "pollutants" : pollutants_data ,
      "daily" : daily_data
   }
   

  printAQIData(data)
  print("------ AQI Data Scrapping Completed  ------")
  return data
  


def printAQIData(data):


  print("------ Daily Air Quality Info ------\n")
  print("AQI -> " , data["daily"][0]["aqi_value"] )
  print("Condition -> " , data["daily"][0]["condition"])
  print("Statement -> " ,data["daily"][0]["statement"])
  print("\n------------ Pollutants ------------\n")

  pollutant_name = []
  for e in data["pollutants"]:
   for keys , value in e.items():
    pollutant_name.append(keys)

  try :
   for i in range(0 , 6):
    print("Pollutant -> " , pollutant_name[i])
    print("Pollutant Index -> " , data["pollutants"][i][f"{pollutant_name[i]}"]["pollutant_index"])
    print("Pollutant concentration -> " , data["pollutants"][i][f"{pollutant_name[i]}"]["pollutant-concentration"])
    print("Condition -> " , data["pollutants"][i][f"{pollutant_name[i]}"]["condition"])
    print("\n------------------------------------\n")
  except Exception as e :
   print(e)
   
# f = open(f"Json\\DehradunAQI.json")
# json_data = json.load(f)

# printData(json_data)




 
  
