from datetime import datetime
from openpyxl import Workbook
import ExporterLogger as logger

workbook = Workbook()
sheet = workbook.active

def export_file(data, folder, file_name, file_type):
    file_type = str(file_type)
    if(file_type.__eq__('.xlsx')):
        export_data_into_excel(data, folder, file_name)
    elif(file_type.__eq__('.docx')):
        export_data_into_word(data, folder, file_name)
    elif(file_type.__eq__('.txt')):
        export_data_into_text(data, folder, file_name)
    else:
        logger.info('File type not supported!\nRaising exception')
        raise ValueError('File type not supported!')

def export_data_into_excel(data, folder, file_name):
    file_name = file_name + '.xlsx'
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)
    for day in data:
        sheet.append(day)
        
    workbook.save(file_path)
    return True

    
def export_data_into_word(data, folder, file_name):
    now = datetime.today()    
    
    file_name = file_name + '.xlsx'
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)
    for day in data:
        sheet.append(day)
        
    workbook.save(file_path)
    return True
    
    
def export_data_into_text(data, folder, file_name):
    now = datetime.today()    
    
    file_name = file_name + '.xlsx'
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)
    for day in data:
        sheet.append(day)
        
    workbook.save(file_path)
    return True