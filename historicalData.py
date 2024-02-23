import json
import openmeteo_requests
from openpyxl import Workbook
import requests_cache
import pandas as pd
from retry_requests import retry

from geopy.geocoders import Nominatim

def scrappingHistoricalData(location):
  location_coordinate = coordinateLocater(location)
  data = meteoApiCall(location , location_coordinate)
  return data

def coordinateLocater(location):

  geolocator = Nominatim(user_agent="MyApp")

  location_coordinate = geolocator.geocode(location)

  return location_coordinate
  

def meteoApiCall(location , location_coordinate):
  cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
  retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
  openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
  url = "https://archive-api.open-meteo.com/v1/archive"
  params = {
	"latitude": location_coordinate.latitude,
	"longitude": location_coordinate.longitude,
	"start_date": "2023-05-06", # YYYY-MM-DD
	"end_date": "2023-08-20",
	"daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "apparent_temperature_max", "apparent_temperature_min", "apparent_temperature_mean", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant", "shortwave_radiation_sum", "et0_fao_evapotranspiration"]
}
  responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
  response = responses[0]
  print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
  print(f"Elevation {response.Elevation()} m asl")
  print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
  print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
  daily = response.Daily()
  daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
  daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
  daily_temperature_2m_mean = daily.Variables(2).ValuesAsNumpy()
  daily_apparent_temperature_max = daily.Variables(3).ValuesAsNumpy()
  daily_apparent_temperature_min = daily.Variables(4).ValuesAsNumpy()
  daily_apparent_temperature_mean = daily.Variables(5).ValuesAsNumpy()
  daily_sunrise = daily.Variables(6).ValuesAsNumpy()
  daily_sunset = daily.Variables(7).ValuesAsNumpy()
  daily_daylight_duration = daily.Variables(8).ValuesAsNumpy()
  daily_sunshine_duration = daily.Variables(9).ValuesAsNumpy()
  daily_precipitation_sum = daily.Variables(10).ValuesAsNumpy()
  daily_rain_sum = daily.Variables(11).ValuesAsNumpy()
  daily_snowfall_sum = daily.Variables(12).ValuesAsNumpy()
  daily_precipitation_hours = daily.Variables(13).ValuesAsNumpy()
  daily_wind_speed_10m_max = daily.Variables(14).ValuesAsNumpy()
  daily_wind_gusts_10m_max = daily.Variables(15).ValuesAsNumpy()
  daily_wind_direction_10m_dominant = daily.Variables(16).ValuesAsNumpy()
  daily_shortwave_radiation_sum = daily.Variables(17).ValuesAsNumpy()
  daily_et0_fao_evapotranspiration = daily.Variables(18).ValuesAsNumpy()



  daily_data_range = {"date": pd.date_range(
	 start = pd.to_datetime(daily.Time(), unit = "s",  utc = True),
	 end = pd.to_datetime(daily.TimeEnd(), unit = "s" , utc = True),
	 freq = pd.Timedelta(seconds = daily.Interval()),
	 inclusive = "left",
  ).strftime('%d-%m-%Y ')
  }

  total_days = len(daily_data_range["date"])
  
  data = []  

  for i in range(total_days):
   daily_data = {
      "Date" : daily_data_range["date"][i],
     "Maximum Temperature (2 m)": daily_temperature_2m_max[i] , 
     "Minimum Temperature (2 m)" : daily_temperature_2m_min[i] ,
     "Mean Temperature (2 m)" : daily_temperature_2m_mean[i] ,
     "Maximum Apparent Temperature (2 m)" : daily_apparent_temperature_max[i] ,
     "Minimum Apparent Temperature (2 m)" : daily_apparent_temperature_min[i] ,
     "Mean Apparent Temperature (2 m)" : daily_apparent_temperature_mean[i] ,
     #"sunrise" : daily_sunrise[i] , #No Data coming from the Meteo
     #"sunset" : daily_sunset[i] , #No Data coming from the Meteo
     "Daylight Duration" : daily_daylight_duration[i] ,
     "Sunshine Duration" : daily_sunshine_duration[i] ,
     "Precipitation Sum" : daily_precipitation_sum[i] ,
     "Rain Sum" : daily_rain_sum[i] ,
     "Snowfall Sum" : daily_snowfall_sum[i] ,
     "Precipitation Hours" : daily_precipitation_hours[i] ,
     "Maximum Wind Speed (10 m)" : daily_wind_speed_10m_max[i] ,
     "Maximum Wind Gusts (10 m)" : daily_wind_gusts_10m_max[i] ,
     "Dominant Wind Direction (10 m)" : daily_wind_direction_10m_dominant[i] ,
     "Shortwave Radiation Sum" : daily_shortwave_radiation_sum[i] ,
     "Reference Evapotranspiration (ET₀)" : daily_et0_fao_evapotranspiration[i]
   }
   data.append(daily_data)

   #daily_dataframe = pd.DataFrame(data)
   #print(daily_dataframe)

  return data

def json_to_excel_hd(data , location):
    
    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Write column headers
    headers = list(data[0].keys())
    ws.append(headers)

    # Write data rows
    for record in data:
     ws.append(list(record.values()))

    # Save workbook
    wb.save(f"Excel/{location.capitalize()}HistoricalData.xlsx")
    
    print("Excel File Successfully Created") 

coordinateLocater("delhi")