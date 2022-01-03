from tkinter import Tk, ttk, PhotoImage, filedialog, messagebox
from tkinter import StringVar, IntVar, NSEW
import ExporterConfig as config
import ExporterRequestProcess, ExporterLogger as logger

logger.info("Exporter Interface initializing...")

QUERY_TYPES = ['Group',
                'Lecturer',
                'Room']

INTERFACE_QUERY_TYPES = ['Класно отделение',
                        'Преподавател',
                        'Зала']

MONTHS = ['January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December']

INTERFACE_MONTHS = ['Януари',
                    'Февруари',
                    'Март',
                    'Април',
                    'Май',
                    'Юни',
                    'Юли',
                    'Август',
                    'Септември',
                    'Октомври',
                    'Ноември',
                    'Декември']

# TODO add new types of data
root_frame = Tk()
group=              IntVar(value=config.group)
query_type=         StringVar(value=config.query_type)
month=              StringVar(value=config.month)
export_directory=   StringVar(value=config.export_directory)

def export():   
    config.update_config(group.get(), query_type.get(), month.get(), export_directory.get())
    logger.info("Exporting data with the following parameters:")
    logger.info("Group: " + str(group.get()))
    logger.info("Query Type: " + query_type.get())
    logger.info("Month: " + month.get())
    logger.info("Default export folder: " + export_directory.get())

    # Export data
    export_result = ExporterRequestProcess.export_monthly_data(group.get(),
                                                query_type.get(),
                                                month.get(),
                                                export_directory.get())    
    if export_result:
        messagebox.showinfo(title="Success", message="Export created succesfully in: \n"+export_directory.get())
        logger.info("Export finished successfuly")

# Create root frame, title, logo and weight for resizing
root_frame.title('Nvna Schedule Exporter')
icon = PhotoImage(file=config.CWD+ r'\logo.png')
root_frame.iconphoto(False, icon)
# TODO weight configurations
root_frame.columnconfigure(index='0 1 2 3 4 5', weight=1)
root_frame.rowconfigure(index='0 1 2 3 4 5 6 7 8 9 10', weight=1)

padx=[20, 10]
pady=[10, 0]
# Създаване на визуални елементи
# Поле за номер
ttk.Label(root_frame, text='Номер:').grid(
    column=0, row=0,
    sticky=NSEW,
    padx=padx, pady=pady)
ttk.Entry(root_frame, textvariable=group, justify='right').grid(
    column=0, columnspan=3, row=1, rowspan=2,
    sticky=NSEW,
    padx=padx)
# Вид заявка
ttk.Label(root_frame, text='Вид заявка:').grid(
    column=0, row=3,
    sticky=NSEW,
    padx=padx, pady=pady)
ttk.OptionMenu(root_frame, query_type, query_type.get(), *INTERFACE_QUERY_TYPES).grid(
    column=0, columnspan=3, row=4, rowspan=2,
    sticky=NSEW,
    padx=padx)
# Месец
ttk.Label(root_frame, text='Месец:').grid(
    column=0, row=7,
    sticky=NSEW,
    padx=padx, pady=pady)
ttk.OptionMenu(root_frame, month, month.get(), *INTERFACE_MONTHS).grid(
    column=0, columnspan=3, row=8, rowspan=2,
    sticky=NSEW,
    padx=padx)
# Директория
ttk.Label(root_frame, text='Директория:').grid(
    column=0, row=10,
    sticky=NSEW,
    padx=padx, pady=pady)
ttk.Entry(root_frame, textvariable=export_directory).grid(
    column=0, columnspan=4, row=11, rowspan=2,
    sticky=NSEW,
    padx=padx)
browse_button_widget = ttk.Button(root_frame, text='Browse...')
browse_button_widget.grid(
    column=4, row=11, rowspan=2,
    sticky=NSEW,
    padx=padx)
browse_button_widget.bind('<ButtonPress>',lambda e: export_directory.set(filedialog.askdirectory()))
# Файл
ttk.Label(root_frame, text='Файл:').grid(
    column=0, row=13,
    sticky=NSEW,
    padx=padx, pady=pady)
ttk.Entry(root_frame, textvariable=export_directory).grid(
    column=0, columnspan=3, row=14, rowspan=2,
    sticky=NSEW,
    padx=padx, pady=[0, 10])
browse_button_widget = ttk.Button(root_frame, text='Export', command=export)
browse_button_widget.grid(
    column=4, row=14, rowspan=2,
    sticky=NSEW,
    padx=padx, pady=[0, 10])

# Loop root frame to visualise elements
root_frame.mainloop()
