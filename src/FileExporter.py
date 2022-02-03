from openpyxl import Workbook
from docx import Document

import ExporterLogger as logger
from ExporterUtil import ExportTypes, TextColors

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

    # Format data and write into a file
    file = open(file_path, 'w', encoding='UTF-8')
    week_index_start = str(weekly_indices[0])
    week_index_end = str(weekly_indices[weekly_indices.__len__()-1])
    if week_index_start == week_index_end:
        file.write("Програма за седмица: " + week_index_start + '\n')
    else:
        file.write("Програма за седмици: " + week_index_start + " - " + week_index_end + '\n')
    d_index = 0
    # For each week
    for w_index in weekly_indices:
        if week_index_start != week_index_end:
            # Write the week index
            file.write('Седмица: ' + str(w_index) + '\n')

        # Get each day's info
        for i in range(7):
            day_info = data[d_index].info()
            if day_info is not None:
                file.write(day_info + '\n')
            d_index+=1

    file.close()

    return True
