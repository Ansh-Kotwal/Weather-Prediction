import json

def jsonOutputFile(location , type , data):
  with open(f"{location.capitalize()}Weather{type}Info.json", "w") as outfile:
    json.dump(data, outfile)
  print("Json File Successfully Created")   
  
