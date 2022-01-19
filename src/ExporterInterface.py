import sys
from tkinter import (
    NSEW,
    NS,
    N,
    Tk,
    ttk,
    IntVar,
    StringVar,
    PhotoImage,
    filedialog,
    messagebox)
from tkinter.constants import BOTH

from PIL import Image, ImageTk

import ExporterConfig as config
import ExporterLogger as logger
import ExporterRequestProcess
import ExporterUtil as util
import ExporterHashChecker as hash_checker
from ExporterUtil import EXPORT_TYPES, INTERFACE_MONTHS, INTERFACE_QUERY_TYPES

# TODO: clean this up or remove it
# logger.info("Exporter Interface initializing...")
# if hash_checker.is_tampered():
#     logger.error("Exporter shutting down!")
#     sys.exit()

root_frame = Tk()
group = IntVar(value=config.group)
query_type = StringVar(value=config.query_type)
month = StringVar(value=config.month)
export_directory = StringVar(value=config.export_directory)
export_file_name = StringVar(value=config.export_file_name)
export_file_type = StringVar(value=config.export_file_type)
first_week = StringVar(value=config.first_week)
last_week = StringVar(value=config.last_week)

# Save loaded data into config file and attempt export
# If succesfull show dialog message and log
def export_monthly():
    config.update_config(group.get(),
                         query_type.get(),
                         month.get(),
                         export_directory.get(),
                         export_file_name.get(),
                         export_file_type.get())

    logger.info("Attempting to export monthly EXCEL report...")
    export_result = ExporterRequestProcess.export_monthly_data(
        group.get(),
        util.get_query_type(query_type.get()),
        util.get_month(month.get()),
        export_directory.get(),
        export_file_name.get(),
        export_file_type.get())

    if export_result:
        messagebox.showinfo(
            title="Success",
            message=export_file_name.get() +
            " created succesfully in: \n" +
            export_directory.get())
        logger.info("Excel export finished successfuly")


# Simple data export to format of choice
def export_simple():
    config.update_config(group.get(),
                         query_type.get(),
                         first_week.get(),
                         last_week.get(),
                         export_directory.get(),
                         export_file_name.get(),
                         export_file_type.get())

    logger.info("Attempting to create simple export...")
    export_result = ExporterRequestProcess.export_monthly_data(
        group.get(),
        util.get_query_type(query_type.get()),
        util.get_month(month.get()),
        export_directory.get(),
        export_file_name.get(),
        export_file_type.get())

    if export_result:
        messagebox.showinfo(
            title="Success",
            message=export_file_name.get() +
            " created succesfully in: \n" +
            export_directory.get())
        logger.info("Excel export finished successfuly")

# Create root frame, title, logo and weight for resizing
root_frame.title('Nvna Schedule Exporter')
root_frame.geometry("650x350")
icon = PhotoImage(file=r'assets\logo.png')
root_frame.iconphoto(True, icon)

# Padding configuration
padx = [20, 10]
padx_button = [60, 60]
padxl = [20, 0]
padyt = [5, 0]
padyb = [0, 20]

# Notebook for frames(tabs) creation
notebook = ttk.Notebook(root_frame, name='notebook')
excel_frame = ttk.Frame(root_frame, name='tab1')
excel_frame.columnconfigure(index='0 1 2 3 4', weight=1)
excel_frame.rowconfigure(index='0 1 2 3 4 5 6 7 8 9 10', weight=1)
export_frame = ttk.Frame(root_frame, name='tab2')
export_frame.columnconfigure(index='0 1 2 3 4', weight=1)
export_frame.rowconfigure(index='0 1 2 3 4 5 6 7 8 9 10', weight=1)
info_frame = ttk.Frame(root_frame, name='tab3')
info_frame.columnconfigure(index='0 1 2 3', weight=1)
info_frame.rowconfigure(index='0 1 2 3 4 5', weight=1)
notebook.add(excel_frame, text='Месечни доклади')
notebook.add(export_frame, text='Седмична програма')
notebook.add(info_frame, text='Седмици')
notebook.select(1)
notebook.pack(expand=1, fill='both')


# ==========================================================================
# ============================ EXCEL_FRAME =================================
# ==========================================================================
# Number
ttk.Label(excel_frame, text='Номер:').grid(
    column=0, row=0,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(excel_frame, textvariable=group).grid(
    column=0, columnspan=4, row=1,
    sticky=NSEW, padx=padx)
# Query type
ttk.Label(excel_frame, text='Вид заявка:').grid(
    column=0, row=2,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.OptionMenu(
    excel_frame,
    query_type,
    query_type.get(),
    *
    INTERFACE_QUERY_TYPES).grid(
        column=0,
        columnspan=4,
        row=3,
        sticky=NSEW,
    padx=padx)
# Month
ttk.Label(excel_frame, text='Месец:').grid(
    column=0, row=4,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.OptionMenu(excel_frame, month, month.get(), *INTERFACE_MONTHS).grid(
    column=0, columnspan=4, row=5,
    sticky=NSEW, padx=padx)
# Image
uni_logo = (Image.open(r'assets\logo.png'))
uni_logo = uni_logo.resize((128, 128), Image.ANTIALIAS)
uni_logo = ImageTk.PhotoImage(uni_logo)
ttk.Label(excel_frame, image=uni_logo).grid(
    column=4, row=0, rowspan=6,
    sticky=NSEW, padx=[70, 20], pady=[20, 0])
# Export directory
ttk.Label(excel_frame, text='Директория:').grid(
    column=0, row=6,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(excel_frame, textvariable=export_directory).grid(
    column=0, columnspan=4, row=7,
    sticky=NSEW, padx=padx)
browse_button_widget = ttk.Button(excel_frame, text='Browse...')
browse_button_widget.grid(
    column=4, row=7,
    sticky=NSEW, padx=padx_button)
browse_button_widget.bind(
    '<ButtonPress>',
    lambda e: export_directory.set(
        filedialog.askdirectory()))
# File name
ttk.Label(excel_frame, text='Файл:').grid(
    column=0, row=9,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(excel_frame, textvariable=export_file_name).grid(
    column=0, columnspan=3, row=10,
    sticky=NSEW, padx=padx, pady=padyb)
export_file_type_widget = ttk.OptionMenu(
    excel_frame, export_file_type, export_file_type.get(), *EXPORT_TYPES)
export_file_type_widget.grid(
    column=3, row=10,
    sticky=NSEW, pady=padyb)
export_file_type_widget.configure(width=5)
browse_button_widget = ttk.Button(excel_frame, text='Export', command=export_monthly)
browse_button_widget.grid(
    column=4, row=10,
    sticky=NSEW, padx=padx_button, pady=padyb)

# ==========================================================================
# ============================ EXPORT_FRAME ================================
# ==========================================================================
# Number
ttk.Label(export_frame, text='Номер:').grid(
    column=0, row=0,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(export_frame, textvariable=group).grid(
    column=0, columnspan=4, row=1,
    sticky=NSEW, padx=padx)
# Query type
ttk.Label(export_frame, text='Вид заявка:').grid(
    column=0, row=2,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.OptionMenu(
    export_frame,
    query_type,
    query_type.get(),
    *
    INTERFACE_QUERY_TYPES).grid(
        column=0,
        columnspan=4,
        row=3,
        sticky=NSEW,
    padx=padx)
# Week range
ttk.Label(export_frame, text='Първа седмица').grid(
    column=0, row=4,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(export_frame, textvariable=first_week).grid(
    column=0, row=5,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Label(export_frame, text='→').grid(
    column=1, row=5,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Label(export_frame, text='Последна седмица').grid(
    column=2, row=4,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(export_frame, textvariable=last_week).grid(
    column=2, row=5,
    sticky=NSEW, padx=padx, pady=padyt)
# Image
ttk.Label(export_frame, image=uni_logo).grid(
    column=4, row=0, rowspan=6,
    sticky=NSEW, padx=[70, 20], pady=[20, 0])
# Export directory
ttk.Label(export_frame, text='Директория:').grid(
    column=0, row=6,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(export_frame, textvariable=export_directory).grid(
    column=0, columnspan=4, row=7,
    sticky=NSEW, padx=padx)
browse_button_widget = ttk.Button(export_frame, text='Browse...')
browse_button_widget.grid(
    column=4, row=7,
    sticky=NSEW, padx=padx_button)
browse_button_widget.bind(
    '<ButtonPress>',
    lambda e: export_directory.set(
        filedialog.askdirectory()))
# File name
ttk.Label(export_frame, text='Файл:').grid(
    column=0, row=9,
    sticky=NSEW, padx=padx, pady=padyt)
ttk.Entry(export_frame, textvariable=export_file_name).grid(
    column=0, columnspan=3, row=10,
    sticky=NSEW, padx=padx, pady=padyb)
export_file_type_widget = ttk.OptionMenu(
    export_frame, export_file_type, export_file_type.get(), *EXPORT_TYPES)
export_file_type_widget.grid(
    column=3, row=10,
    sticky=NSEW, pady=padyb)
export_file_type_widget.configure(width=5)
browse_button_widget = ttk.Button(export_frame, text='Export', command=export_monthly)
browse_button_widget.grid(
    column=4, row=10,
    sticky=NSEW, padx=padx_button, pady=padyb)
# ==========================================================================
# ============================ INFO_FRAME ==================================
# ==========================================================================
week_indices = util.get_weekly_indices(config.year)
for month_name, index in zip(util.INTERFACE_MONTHS, range(12)):
    ttk.Label(info_frame, text=month_name).grid(
        column=index % 4, row=(index // 4) * 2,
        sticky=NS
    )
    ttk.Label(info_frame, text=week_indices[index]).grid(
        column=index % 4, row=(index // 4) * 2 + 1,
        sticky=N
    )
# ==========================================================================
# Loop root frame to visualise elements
root_frame.mainloop()
