from datetime import datetime
import os
from openpyxl import Workbook
from ExporterUtil import ExportTypes
import ExporterLogger as logger

workbook = Workbook()
sheet = workbook.active

def export_file(data, folder, file_name, file_type):
    file_type = str(file_type)
    if(file_type.__eq__(ExportTypes.EXCEL)):
        return export_data_into_excel(data, folder, file_name)
    elif(file_type.__eq__(ExportTypes.WORD)):
        return export_data_into_word(data, folder, file_name)
    elif(file_type.__eq__(ExportTypes.PLAINTEXT)):
        return export_data_into_text(data, folder, file_name)
    else:
        logger.info('File type not supported!\nRaising exception')
        raise ValueError('File type not supported!')

def export_data_into_excel(data, folder, file_name):
    file_name = file_name + ExportTypes.EXCEL
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)

    for day in data:
        sheet.append(day)
        
    workbook.save(file_path)
    return True

    
def export_data_into_word(data, folder, file_name):
    file_name = file_name + ExportTypes.WORD
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)

    for day in data:
        sheet.append(day)
        
    workbook.save(file_path)
    return True
    
    
def export_data_into_text(data, folder, file_name):
    file_name = file_name + ExportTypes.PLAINTEXT
    file_path = folder + '\\' + file_name
    logger.info("Creating " + file_name + " in: " + folder)

    file = open(file_path, 'w', encoding='UTF-8')
    for day in data:
        file.write(str(day) + '\n')
    file.close()

    return True