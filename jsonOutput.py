import json

def jsonOutputFile(location , data , name):
  with open(f"Json\\{location.capitalize()}{name}.json", "w") as outfile:
    json.dump(data, outfile)
  print("\n------ Json File Successfully Created ------")   
  
