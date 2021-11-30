
from tkinter import *;
from tkinter import ttk
from tkinter import filedialog;
from datetime import date;
from ExporterInputValidator import ExporterInputValidator
import os
import ExporterRequestProcess;

class ExporterUI:
    # Create root frame and add a title to it
    root_frame = Tk();
    root_frame.title("Nvna Schedule Exporter");
    icon = PhotoImage(file="D:\Workspace\ВВМУ\Курсов Проект\\assets\logo.png");
    root_frame.iconphoto(False, icon);
    root_frame.columnconfigure(index="0 1 2 3", weight=1)
    root_frame.rowconfigure(index="0 1 2 3 4 5", weight=1)

    # Create Tkinter vars to be later used as request parameters 
    global group
    group = IntVar(value=0)
    global query_type
    query_type = StringVar(value="group")
    global week
    week = IntVar(value=date.today().isocalendar().week);
    global default_export_folder
    default_export_folder = StringVar(value=os.getcwd())

    # Create validation wrappers for request parameters
    validate_group_wrapper = (root_frame.register(ExporterInputValidator.validate_group), '%P')
    validate_query_type_wrapper = (root_frame.register(ExporterInputValidator.validate_query_type), '%P')
    validate_week_wrapper = (root_frame.register(ExporterInputValidator.validate_week), '%P')
    
    # Create parameter fields and labels
    # TODO:FUNCTIONALITY - go over each element and set its corresponding type and config
    # Group Number   
    ttk.Label(root_frame, text='Group:').grid(column=0, row=0, sticky=(N, E, S, W), padx="20 10", pady="10 5")
    ttk.Entry(root_frame, textvariable=group, justify='right').grid(column=1, columnspan=3, row=0, sticky=(N, E, S, W), padx="10 20", pady="10 5")
    
    # ttk.Entry(mainFrame, textvariable=group, validate='key', validatecommand=(validate_group_wrapper, queryType)).grid(column=0, row=1)
    # Query Type
    ttk.Label(root_frame, text='Type:').grid(column=0, row=1, sticky=(N, E, S, W), padx="20 10", pady="5 5")
    ttk.Entry(root_frame, textvariable=query_type, justify='right').grid(column=1, columnspan=3, row=1, sticky=(N, E, S, W), padx="10 20", pady="5 5")
    # ttk.Entry(mainFrame, textvariable=queryType, validate='key', validatecommand=validate_query_type_wrapper).grid(column=1, row=1)
    # OptionMenu(mainFrame, queryType, 'Group', 'Lecturer', 'Week').grid(column=1, row=1)
    # Week Number
    # TODO: find a date library and get current week number
    ttk.Label(root_frame, text='Week:').grid(column=0, row=2, sticky=(N, E, S, W), padx="20 10", pady="5 5")
    ttk.Entry(root_frame, textvariable=week, justify='right').grid(column=1, columnspan=3, row=2, sticky=(N, E, S, W), padx="10 20", pady="5 5")
    # ttk.Entry(mainFrame, textvariable=week, validate='key', validatecommand=validate_week_wrapper).grid(column=2, row=1)

    # Export functionality
    ttk.Label(root_frame, text="Output folder:").grid(column=0, row=3, sticky=(N, E, S, W), padx="20 10", pady="5 5")
    ttk.Entry(root_frame, textvariable=default_export_folder, state='readonly').grid(column=1, columnspan=2, row=3, sticky=(N, E, S, W), padx="10 5", pady="5 5")
    browse_button_widget = ttk.Button(root_frame, text="Browse...")
    browse_button_widget.grid(column=3, row=3, sticky=(N, E, S, W), padx="5 20", pady="5 5")
    browse_button_widget.bind('<ButtonPress>', lambda e: default_export_folder.set(filedialog.askdirectory()))

    export_button_widget = ttk.Button(root_frame, text="Export")
    export_button_widget.grid(column=1, columnspan=2, row=5, sticky=(N, E, S, W), padx="10 0", pady="5 10")
    export_button_widget.bind('<ButtonPress>', lambda e: ExporterRequestProcess.get_weekly_data(group.get(), query_type.get(), week.get()))

    
    # Loop root frame to visualise elements
    root_frame.mainloop()

    # TODO:USABILITY add exact date calculation based on week number

    # TODO:FUNCTIONALITY Add field validations
    # group length dependening on type
    # type from an enum list of predetermined string values
    # week - numerical value of max 52