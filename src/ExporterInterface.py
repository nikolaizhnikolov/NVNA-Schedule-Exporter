from tkinter import (NSEW, IntVar, PhotoImage, StringVar, Tk, filedialog,
                     messagebox, ttk)
from tkinter.constants import BOTH

from PIL import Image, ImageTk

import ExporterConfig as config
import ExporterLogger as logger
import ExporterRequestProcess
import ExporterUtil as util
from ExporterUtil import INTERFACE_MONTHS, INTERFACE_QUERY_TYPES

logger.info("Exporter Interface initializing...")

root_frame = Tk()
group=              IntVar(value=config.group)
query_type=         StringVar(value=config.query_type)
month=              StringVar(value=config.month)
export_directory=   StringVar(value=config.export_directory)
export_file_name=   StringVar(value=config.export_file_name)

# Save loaded data into config file and attempt export
# If succesfull show dialog message and log
def export():   
    config.update_config(group.get(), query_type.get(), month.get(), export_directory.get(), export_file_name.get())
    logger.info("Creating export with the following parameters:")
    logger.info("Group: " +         str(group.get()))
    logger.info("Query type: " +    query_type.get())
    logger.info("Month: " +         month.get())
    logger.info("Export directory: " +         export_directory.get())
    logger.info("Export file name: " +   export_file_name.get())

    export_result = ExporterRequestProcess.export_monthly_data(group.get(),
                                                util.get_query_type(query_type.get()),
                                                util.get_month(month.get()),
                                                export_directory.get(),
                                                export_file_name.get())    
    if export_result:
        messagebox.showinfo(title="Success", message=export_file_name.get()+" created succesfully in: \n"+export_directory.get())
        logger.info("Excel export finished successfuly")

# Create root frame, title, logo and weight for resizing
root_frame.title('Nvna Schedule Exporter')
root_frame.geometry("650x350")
icon = PhotoImage(file=r'assets\logo.png')
root_frame.iconphoto(True, icon)

root_frame.columnconfigure(index='0 1 2 3 4', weight=1)
root_frame.rowconfigure(index='0 1 2 3 4 5 6 7 8 9 10', weight=1)

# Padding configuration for reuse
padx=       [20, 10]
padx_button=[60, 60]
padxl=      [20, 0]
padyt=      [5, 0]
padyb=      [0, 20]

# Visual elements creation
# Notebook for containing tabs and frame(tab) creation
# notebook=ttk.Notebook(root_frame, name='monthly reports')
# excel_frame=ttk.Frame(root_frame, name='tab1')
# excel_frame.columnconfigure(index='0 1 2 3 4', weight=1)
# excel_frame.rowconfigure(index='0 1 2 3 4 5 6 7 8 9 10', weight=1)
# notebook.add(excel_frame, text='Месечни доклади')
# notebook.select(0)
# notebook.pack(expand=1, fill='both')
# Number
ttk.Label(root_frame, text='Номер:').grid(
    column=0, row=0,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.Entry(root_frame, textvariable=group).grid(
    column=0, columnspan=4, row=1, 
    sticky=NSEW,
    padx=padx)
# Query type
ttk.Label(root_frame, text='Вид заявка:').grid(
    column=0, row=2,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.OptionMenu(root_frame, query_type, query_type.get(), *INTERFACE_QUERY_TYPES).grid(
    column=0, columnspan=4, row=3,
    sticky=NSEW,
    padx=padx)
# Month
ttk.Label(root_frame, text='Месец:').grid(
    column=0, row=4,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.OptionMenu(root_frame, month, month.get(), *INTERFACE_MONTHS).grid(
    column=0, columnspan=4, row=5,
    sticky=NSEW,
    padx=padx)
# Image
uni_logo=(Image.open(r'assets\logo.png'))
uni_logo= uni_logo.resize((128, 128), Image.ANTIALIAS)
uni_logo= ImageTk.PhotoImage(uni_logo)
ttk.Label(root_frame, image=uni_logo).grid(
    column=4, row=0, rowspan=6,
    sticky=NSEW, 
    padx=[70, 20], pady=[20, 0])
# Export directory
ttk.Label(root_frame, text='Директория:').grid(
    column=0, row=6,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.Entry(root_frame, textvariable=export_directory).grid(
    column=0, columnspan=4, row=7,
    sticky=NSEW,
    padx=padx)
browse_button_widget = ttk.Button(root_frame, text='Browse...')
browse_button_widget.grid(
    column=4, row=7,
    sticky=NSEW,
    padx=padx_button)
browse_button_widget.bind('<ButtonPress>',lambda e: export_directory.set(filedialog.askdirectory()))
# File name
ttk.Label(root_frame, text='Файл:').grid(
    column=0, row=9,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.Entry(root_frame, textvariable=export_file_name).grid(
    column=0, columnspan=3, row=10,
    sticky=NSEW,
    padx=padx, pady=padyb)
ttk.Label(root_frame, text=".xlsx").grid(
    column=3, row=10,
    sticky=NSEW,
    pady=padyb
)
browse_button_widget = ttk.Button(root_frame, text='Export', command=export)
browse_button_widget.grid(
    column=4, row=10,
    sticky=NSEW,
    padx=padx_button, pady=padyb)

# Loop root frame to visualise elements
root_frame.mainloop()
