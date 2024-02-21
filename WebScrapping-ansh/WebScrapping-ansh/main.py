from selenium import webdriver
import scrapper_v1

class main:
    def main():
    #    chrome_options = webdriver.ChromeOptions()
    #    chrome_options.add_argument("--headless")
    #    chrome_options.add_argument(
    #    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

        driver = webdriver.Chrome()
        driver.get("https://www.accuweather.com/")
        serverRun = scrapper_v1.Scrapping

        location = input("Enter location => ")
    #  location = "Dehradun"
    
        serverRun.scrappingData(driver , location)


# Class run
test_instance = main
con = test_instance.main()

# pip \\\\\
# pip install -r requirements.txt\
