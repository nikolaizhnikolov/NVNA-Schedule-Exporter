from datetime import date, datetime
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

def export_data_into_excel(data, month, folder):
    now = datetime.today()    
    
    filename = '/NvnaExport_' + month + '_' + str(date(now.year, now.month, now.day)) + '.xlsx'
    fullpath = folder + filename
    for day in data:
        sheet.append(day)
        
    workbook.save(fullpath)
    return True