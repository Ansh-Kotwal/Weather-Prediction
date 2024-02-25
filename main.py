import scrapper_v1 

class main:
    def main():
     serverRun = scrapper_v1.Scrapping

     print("\n########################################################################################################################################\n")
     location = input("-> Enter location => ")
     serverRun.scrappingData(location)
     print("\n------ All Data Sucessfully Scrapped/Fetched ------")
     print("\n########################################################################################################################################\n")


# Class run
test_instance = main
con = test_instance.main()

# pip 
# pip install -r requirements.txt
