from dailyData import getData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class



def getJson(browser , daily_url ):
    print("inside getJson function")
    
    index = daily_url.find("city=")
    daily_url = daily_url[:index]
    
    jsonData = []
    
    for i in range(1, 10  ):
        main_card_url = daily_url+"day="+str(i)
        data = {
            "day "+str(i) : getData(browser,main_card_url)
        }
        jsonData.append(data)
        
    
    return jsonData
    
    
    