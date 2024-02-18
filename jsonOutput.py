import json

def jsonOutputFile(location , data):
  with open(f"{location.capitalize()}WeatherInfo.json", "w") as outfile:
    json.dump(data, outfile)
  print("Json File Successfully Created")   
  
