from tkinter import Tk, ttk, PhotoImage, filedialog, messagebox
from tkinter import StringVar, IntVar, NSEW
from PIL import Image, ImageTk 
from ExporterUtil import INTERFACE_QUERY_TYPES, INTERFACE_MONTHS
import ExporterConfig as config
import ExporterRequestProcess, ExporterLogger as logger

logger.info("Exporter Interface initializing...")

root_frame = Tk()
group=              IntVar(value=config.group)
query_type=         StringVar(value=config.query_type)
month=              StringVar(value=config.month)
export_directory=   StringVar(value=config.export_directory)
export_file_name=   StringVar(value=config.export_file_name)

def export():   
    config.update_config(group.get(), query_type.get(), month.get(), export_directory.get(), export_file_name.get())
    logger.info("Exporting data with the following parameters:")
    logger.info("Group: " + str(group.get()))
    logger.info("Query Type: " + query_type.get())
    logger.info("Month: " + month.get())
    logger.info("Default export folder: " + export_directory.get())
    logger.info("Export file name: " + export_file_name.get())

    # Export data
    export_result = ExporterRequestProcess.export_monthly_data(group.get(),
                                                query_type.get(),
                                                month.get(),
                                                export_directory.get(),
                                                export_file_name.get())    
    if export_result:
        messagebox.showinfo(title="Success", message=export_file_name.get()+"created succesfully in: \n"+export_directory.get())
        logger.info("Export finished successfuly")

# Create root frame, title, logo and weight for resizing
root_frame.title('Nvna Schedule Exporter')
root_frame.geometry("650x350")
icon = PhotoImage(file=config.CWD+ r'\logo.png')
root_frame.iconphoto(True, icon)

root_frame.columnconfigure(index='0 1 2 3 4', weight=1)
root_frame.rowconfigure(index='0 1 2 3 4 5 6 7 8 9 10', weight=1)

# Конфигурация на отстояния за лесно преизползване
padx=[20, 10]
padx_button=[60, 60]
padxl=[20, 0]
padyt=[5, 0]
padyb=[0, 20]
# Създаване на визуални елементи
# Поле за номер
ttk.Label(root_frame, text='Номер:').grid(
    column=0, row=0,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.Entry(root_frame, textvariable=group).grid(
    column=0, columnspan=4, row=1, 
    sticky=NSEW,
    padx=padx)
# Вид заявка
ttk.Label(root_frame, text='Вид заявка:').grid(
    column=0, row=2,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.OptionMenu(root_frame, query_type, query_type.get(), *INTERFACE_QUERY_TYPES).grid(
    column=0, columnspan=4, row=3,
    sticky=NSEW,
    padx=padx)
# Месец
ttk.Label(root_frame, text='Месец:').grid(
    column=0, row=4,
    sticky=NSEW,
    padx=padx, pady=padyt)
ttk.OptionMenu(root_frame, month, month.get(), *INTERFACE_MONTHS).grid(
    column=0, columnspan=4, row=5,
    sticky=NSEW,
    padx=padx)
# Изображение
uni_logo=(Image.open("logo.png"))
uni_logo= uni_logo.resize((128, 128), Image.ANTIALIAS)
uni_logo= ImageTk.PhotoImage(uni_logo)
ttk.Label(root_frame, image=uni_logo).grid(
    column=4, row=0, rowspan=6,
    sticky=NSEW, 
    padx=[70, 20], pady=[20, 0])
# Директория
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
# Файл
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
