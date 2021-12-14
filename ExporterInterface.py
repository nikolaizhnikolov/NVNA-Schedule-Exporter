from tkinter import Tk, ttk, PhotoImage, filedialog
from tkinter import StringVar, IntVar, NSEW
import ExporterConfig as config
import ExporterRequestProcess, ExporterLogger as logger

logger.info("Exporter Interface initializing...")

QUERY_TYPES = ['Group',
                'Lecturer',
                'Week']

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

root_frame = Tk()
group=              IntVar(value=config.group)
query_type=         StringVar(value=config.query_type)
month=              StringVar(value=config.month)
export_directory=   StringVar(value=config.export_directory)

def export():   
        
    logger.info("Exporting data with the following parameters:")
    logger.info("Group: " + str(group.get()))
    logger.info("Query Type: " + query_type.get())
    logger.info("Month: " + month.get())
    logger.info("Default export folder: " + export_directory.get())

    # Export data
    ExporterRequestProcess.export_monthly_data(group.get(),
                                                query_type.get(),
                                                month.get(),
                                                export_directory.get())    
    logger.info("Export finished successfuly")

# Create root frame, title, logo and weight for resizing
root_frame.title('Nvna Schedule Exporter')
icon = PhotoImage(file=r'D:\Workspace\ВВМУ\Курсов Проект\logo.png')
root_frame.iconphoto(False, icon)
root_frame.columnconfigure(index='0 1 2 3', weight=1)
root_frame.rowconfigure(index='0 1 2 3 4 5', weight=1)

# Create parameter fields and labels
# Group Number
ttk.Label(root_frame, text='Group:').grid(
    column=0, row=0,
    sticky=(NSEW),
    padx='20 10', pady='10 5')
ttk.Entry(root_frame, textvariable=group, justify='right').grid(
    column=1, columnspan=3, row=0,
    sticky=(NSEW),
    padx='10 20', pady='10 5')
# Query Type
ttk.Label(root_frame, text='Type:').grid(
    column=0, row=1,
    sticky=(NSEW),
    padx='20 10', pady='5 5')
ttk.OptionMenu(root_frame, query_type, query_type.get(), *QUERY_TYPES).grid(
    column=1, columnspan=3, row=1,
    sticky=(NSEW),
    padx='10 20',
    pady='5 5')
# Month
ttk.Label(root_frame, text='Month:').grid(
    column=0, row=2,
    sticky=(NSEW),
    padx='20 10', pady='5 5')
ttk.OptionMenu(root_frame, month, month.get(), *MONTHS).grid(
    column=1, columnspan=3, row=2,
    sticky=(NSEW),
    padx='10 20', pady='5 5')
# Output Folder
ttk.Label(root_frame, text='Output folder:').grid(
    column=0, row=3,
    sticky=(NSEW),
    padx='20 10', pady='5 5')
ttk.Entry(root_frame, textvariable=export_directory).grid(
    column=1, columnspan=2, row=3,
    sticky=(NSEW),
    padx='10 5', pady='5 5')
browse_button_widget = ttk.Button(root_frame, text='Browse...')
browse_button_widget.grid(
    column=3, row=3,
    sticky=(NSEW),
    padx='5 20', pady='5 5')
browse_button_widget.bind('<ButtonPress>',lambda e: export_directory.set(filedialog.askdirectory()))
# Export Button
export_button_widget = ttk.Button(root_frame, text='Export', command=export)
export_button_widget.grid(
    column=1, columnspan=2, row=5,
    sticky=(NSEW),
    padx='10 5', pady='5 10')

# Loop root frame to visualise elements
root_frame.mainloop()
