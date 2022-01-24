from openpyxl import Workbook
from docx import Document

import ExporterLogger as logger
from ExporterUtil import ExportTypes

workbook = Workbook()
sheet = workbook.active

# TODO: refactor this whole file
# have a single export into excel for monthly reports
# then a different function for each simple export,
#   which will format the data inside the function body depending on query_type


def export_simple_report(data, folder, file_name, file_type, weekly_indices):
    file_type = str(file_type)
    if(file_type.__eq__(ExportTypes.EXCEL)):
        return export_data_into_excel(data, folder, file_name, weekly_indices)
    elif(file_type.__eq__(ExportTypes.WORD)):
        return export_data_into_word(data, folder, file_name, weekly_indices)
    elif(file_type.__eq__(ExportTypes.PLAINTEXT)):
        return export_data_into_text(data, folder, file_name, weekly_indices)
    else:
        logger.info('File type not supported!\nRaising exception')
        raise ValueError('File type not supported!')
    
    
def export_monthly_report(data, folder, file_name):
    file_name = file_name + ExportTypes.EXCEL
    file_path = folder + '\\' + file_name
    logger.info("Creating Excel Document: " + file_name + " in: " + folder)

    for day in data:
        sheet.append(day)

    workbook.save(file_path)
    return True    


def export_data_into_excel(data, folder, file_name, weekly_indices):
    file_name = file_name + ExportTypes.EXCEL
    file_path = folder + '\\' + file_name
    logger.info("Creating Excel Document: " + file_name + " in: " + folder)

    for day in data:
        sheet.append(day)

    workbook.save(file_path)
    return True


def export_data_into_word(data, folder, file_name, weekly_indices):
    file_name = file_name + ExportTypes.WORD
    file_path = folder + '\\' + file_name
    logger.info("Creating Word Document: " + file_name + " in: " + folder)

    file = Document()
    file.add_heading('Програма за месец ' + 'Х')

    for day in data:
        file.add_paragraph(day)

    file.save(file_path)
    return True


def export_data_into_text(data, folder, file_name, weekly_indices):
    file_name = file_name + ExportTypes.PLAINTEXT
    file_path = folder + '\\' + file_name
    logger.info("Creating Text File: " + file_name + " in: " + folder)

    file = open(file_path, 'w', encoding='UTF-8')
    d_index = 0
    for w_index in weekly_indices:
        file.write('Седмица ' + str(w_index) + ':')
        first_day=data[d_index]
        last_day=data[d_index + 6]
        file.write(first_day[1] + ' - ' + last_day[1] + '\n')

        for i in range(7):
            day = data[d_index]

            file.write(str(day) + '\n')

            d_index+=1
    # for day in data:
    #     file.write(str(day) + '\n')

    file.close()

    return True
