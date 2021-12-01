from tkinter import Tk, ttk, PhotoImage, filedialog
from tkinter import StringVar, IntVar, NSEW
from datetime import date
import os
import configparser
import ExporterRequestProcess

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

CWD = os.getcwd()

config_parser = configparser.RawConfigParser()
config_parser.read('exporter_config.cfg', encoding='UTF-8')

root_frame = Tk()
group=              IntVar(value=config_parser.get('request_parameters', 'group', fallback='0'))
query_type=         StringVar(value=config_parser.get('request_parameters', 'query_type', fallback=QUERY_TYPES[0]))
month=              StringVar(value=config_parser.get('request_parameters', 'month', fallback=date.today().strftime('%B')))
export_directory=   StringVar(value=config_parser.get('request_parameters', 'export_directory', fallback=CWD))

def export():
    # Save request parameters into cfg for next use
    config_parser.set('request_parameters', 'group', group.get())
    config_parser.set('request_parameters', 'query_type', query_type.get())
    config_parser.set('request_parameters', 'month', month.get())
    config_parser.set('request_parameters', 'export_directory', export_directory.get())
    with open('exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)        

    # Export data
    ExporterRequestProcess.export_monthly_data(group.get(),
                                                query_type.get(),
                                                month.get(),
                                                export_directory.get())


# Create root frame, title, logo and weight for resizing
root_frame.title('Nvna Schedule Exporter')
icon = PhotoImage(file=r'D:\Workspace\ВВМУ\Курсов Проект\assets\logo.png')
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
export_button_widget = ttk.Button(root_frame, text='Export')
export_button_widget.grid(
    column=1, columnspan=2, row=5,
    sticky=(NSEW),
    padx='10 5', pady='5 10')
export_button_widget.bind('<ButtonPress>',lambda e: export())

# Loop root frame to visualise elements
root_frame.mainloop()
