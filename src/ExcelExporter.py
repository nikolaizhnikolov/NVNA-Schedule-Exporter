from datetime import date, datetime
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

def export_data_into_excel(data, month, folder, file_name):
    now = datetime.today()    
    
    file_name = file_name + '.xlsx'
    fullpath = folder + file_name
    for day in data:
        sheet.append(day)
        
    workbook.save(fullpath)
    return True