from openpyxl import Workbook
import os

def flatten_json(json_data):
    flattened_data = []
    for record in json_data:
        for key, value in record.items():
            day_number = key
            day = value['day']
            night = value['night']
            flattened_record = {
                'Day': day_number,
                'Day Temperature': day['temp'],
                'Max UV Index': day['max_uv_index'],
                'Day Wind': day['wind'],
                'Day Wind Gust': day['wind_gust'],
                'Day Probability of Precipitation': day['probability_of_precipitation'],
                'Day Probability of Thunderstorms': day['probability_of_thunderstorms'],
                'Day Precipitation': day['Precipitation'],
                'Day Cloud Cover': day['cloud_cover'],
                'Day Remark': day['remark'],
                'Night Temperature': night['temp'],
                'Night Wind': night['wind'],
                'Night Wind Gust': night['wind_gust'],
                'Night Probability of Precipitation': night['probability_of_precipitation'],
                'Night Probability of Thunderstorms': night['probability_of_thunderstorms'],
                'Night Precipitation': night['Precipitation'],
                'Night Cloud Cover': night['cloud_cover'],
                'Night Remark': night['remark']
            }
            flattened_data.append(flattened_record)
    return flattened_data

# f = open("DehradunWeatherInfo.json")

# json_data = json.load(f)


def json_to_excel(json_data, excel_file):
    flattened_data = flatten_json(json_data)
    
    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Write column headers
    headers = list(flattened_data[0].keys())
    ws.append(headers)

    # Write data rows
    for record in flattened_data:
        ws.append(list(record.values()))

    # Save workbook
    wb.save(excel_file)

    # Open Excel file
   # os.system(f'start excel "{excel_file}"')

# json_to_excel(json_data, 'output_excel_file.xlsx')
