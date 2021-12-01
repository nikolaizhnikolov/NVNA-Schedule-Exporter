from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

def export_data_into_excel(data):
    return