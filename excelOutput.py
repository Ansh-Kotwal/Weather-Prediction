from openpyxl import Workbook

def json_to_excel(json_data, excel_file):
    #print(flattened_data)
    
    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Write column headers
    headers = list(json_data[0].keys())
    ws.append(headers)

    # Write data rows
    for record in json_data:
        ws.append(list(record.values()))

    # Save workbook
    wb.save(f"Excel/{excel_file}")

    # Open Excel file
   # os.system(f'start excel "{excel_file}"')
    
    print("Excel File Successfully Created") 

# json_to_excel(json_data, 'output_excel_file.xlsx')
