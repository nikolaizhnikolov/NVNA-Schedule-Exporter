from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import date
import os
import configparser
import ExporterRequestProcess

global cwd
cwd = os.getcwd()

global config_parser
config_parser = configparser.RawConfigParser()
config_parser.read("exporter_config.cfg", encoding='UTF-8')
    
def export():
    # Save request parameters 
    config_parser.set('request_parameters', 'group', group.get())
    config_parser.set('request_parameters', 'query_type', query_type.get())
    config_parser.set('request_parameters', 'month', month.get())
    config_parser.set('request_parameters', 'export_directory', export_directory.get())
    with open('exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)
    # ExporterRequestProcess.export_monthly_data()
        
class ExporterUI:    
    # Create root frame, title, logo and weight for resizing
    root_frame = Tk();
    root_frame.title("Nvna Schedule Exporter");
    icon = PhotoImage(file="D:\Workspace\ВВМУ\Курсов Проект\\assets\logo.png");
    root_frame.iconphoto(False, icon);
    root_frame.columnconfigure(index="0 1 2 3", weight=1)
    root_frame.rowconfigure(index="0 1 2 3 4 5", weight=1)

    # Create Tkinter vars for request parameters   
    global group
    global query_type
    global month
    global export_directory
    
    group = IntVar(value=config_parser.get('request_parameters', 'group', fallback='0'))
    query_type = StringVar(value=config_parser.get('request_parameters', 'query_type', fallback='Group'))
    month = StringVar(value=config_parser.get('request_parameters', 'month', fallback=date.today().strftime('%B')));
    export_directory = StringVar(value=config_parser.get('request_parameters', 'export_directory', fallback=cwd))
    
    # Create parameter fields and labels
    # TODO:FUNCTIONALITY - go over each element and set its corresponding type and config
    # Group Number   
    ttk.Label(root_frame, text='Group:').grid(column=0, row=0, sticky=(N, E, S, W), padx="20 10", pady="10 5")
    ttk.Entry(root_frame, textvariable=group, justify='right').grid(column=1, columnspan=3, row=0, sticky=(N, E, S, W), padx="10 20", pady="10 5")
    
    # Query Type
    ttk.Label(root_frame, text='Type:').grid(column=0, row=1, sticky=(N, E, S, W), padx="20 10", pady="5 5")
    # ttk.Entry(root_frame, textvariable=query_type, justify='right').grid(column=1, columnspan=3, row=1, sticky=(N, E, S, W), padx="10 20", pady="5 5")
    type_list_widget = ttk.OptionMenu(root_frame, query_type, query_type.get(), "Group", "Lecturer", "Week")
    type_list_widget.grid(column=1, columnspan=3,row=1, sticky=(N, E, S, W), padx="10 20", pady="5 5")
    type_list_widget.config()
    # Week Number
    ttk.Label(root_frame, text='Week:').grid(column=0, row=2, sticky=(N, E, S, W), padx="20 10", pady="5 5")
    ttk.Entry(root_frame, textvariable=month, justify='right').grid(column=1, columnspan=3, row=2, sticky=(N, E, S, W), padx="10 20", pady="5 5")

    # Export functionality
    ttk.Label(root_frame, text="Output folder:").grid(column=0, row=3, sticky=(N, E, S, W), padx="20 10", pady="5 5")
    ttk.Entry(root_frame, textvariable=export_directory, state='readonly').grid(column=1, columnspan=2, row=3, sticky=(N, E, S, W), padx="10 5", pady="5 5")
    browse_button_widget = ttk.Button(root_frame, text="Browse...")
    browse_button_widget.grid(column=3, row=3, sticky=(N, E, S, W), padx="5 20", pady="5 5")
    browse_button_widget.bind('<ButtonPress>', lambda e: export_directory.set(filedialog.askdirectory()))

    export_button_widget = ttk.Button(root_frame, text="Export")
    export_button_widget.grid(column=1, columnspan=2, row=5, sticky=(N, E, S, W), padx="10 5", pady="5 10")
    export_button_widget.bind('<ButtonPress>', lambda e: export())
    
    # Loop root frame to visualise elements
    root_frame.mainloop()

    # TODO:USABILITY add exact date calculation based on week number

    # TODO:FUNCTIONALITY Add field validations
    # group length dependening on type
    # type from an enum list of predetermined string values
    # week - numerical value of max 52