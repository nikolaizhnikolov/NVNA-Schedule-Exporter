from datetime import datetime
from openpyxl import Workbook
import ExporterLogger as logger

workbook = Workbook()
sheet = workbook.active

def export_data_into_excel(data, month, folder, file_name):
    now = datetime.today()    
    
    file_name = file_name + '.xlsx'
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)
    for day in data:
        sheet.append(day)
        
    workbook.save(file_path)
    return True