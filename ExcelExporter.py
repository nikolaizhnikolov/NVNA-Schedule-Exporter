from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

def save_data_into_sheet(data):
    return