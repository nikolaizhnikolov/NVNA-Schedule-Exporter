import requests;
from tkinter import *;
from tkinter import ttk;
from datetime import date;
from ExporterInputValidator import ExporterInputValidator;

class ExporterUI:
    # Create root frame and add a title to it
    rootFrame = Tk();
    rootFrame.title("Nvna Schedule Exporter");
    icon = PhotoImage(file="D:\Workspace\ВВМУ\Курсов Проект\\assets\logo.png");
    rootFrame.iconphoto(False, icon);
    # rootFrame.columnconfigure(0, weight=1);
    # rootFrame.rowconfigure(0, weight=1);

    # Create main frame to hold all widgets
    mainFrame = ttk.Frame(rootFrame, padding="10")
    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    # TODO: set main frame size if needed
    # mainFrame.config(width=800, height=400)
    # mainFrame.grid_propagate(False);

    # Create Tkinter vars to be later used as request parameters 
    group = IntVar()
    queryType = StringVar()
    queryType.set("Group")
    week = IntVar(value=date.today().isocalendar().week); 
    # Create validation wrappers for request parameters
    validate_group_wrapper = (rootFrame.register(ExporterInputValidator.validate_group), '%P')
    validate_query_type_wrapper = (rootFrame.register(ExporterInputValidator.validate_query_type), '%P')
    validate_week_wrapper = (rootFrame.register(ExporterInputValidator.validate_week), '%P')
    
    # Create parameter fields and labels
    # TODO:FUNCTIONALITY - go over each element and set its corresponding type and config
    # Group Number   
    ttk.Label(mainFrame, text='Group').grid(column=0, row=0)
    ttk.Entry(mainFrame, textvariable=group, validate='key', validatecommand=(validate_group_wrapper, queryType)).grid(column=0, row=1)
    # Query Type
    ttk.Label(mainFrame, text='Type').grid(column=1, row=0)
    ttk.Entry(mainFrame, textvariable=queryType, validate='key', validatecommand=validate_query_type_wrapper).grid(column=1, row=1)
    # OptionMenu(mainFrame, queryType, 'Group', 'Lecturer', 'Week').grid(column=1, row=1)
    # Week Number
    # TODO: find a date library and get current week number
    ttk.Label(mainFrame, text='Week').grid(column=2, row=0)
    ttk.Entry(mainFrame, textvariable=week, validate='key', validatecommand=validate_week_wrapper).grid(column=2, row=1)


    # Export functionality
    ttk.Label(mainFrame, text="Output folder:").grid(column=0, row=2)
    ttk.Button(mainFrame, text="Browse...").grid(column=1, row=2);
    ttk.Entry(mainFrame, state='readonly').grid(column=0, columnspan=2, row=3)
    ttk.Button(mainFrame, text="Export").grid(column=2, row=3, rowspan=2)
    # TODO:USABILITY add exact date calculation based on week number

    # TODO:FUNCTIONALITY Add field validations
    # group length dependening on type
    # type from an enum list of predetermined string values
    # week - numerical value of max 52

    # mainFrame.config(width=800, height=400)
    # Create export functionality

    # Loop root frame to visualise elements
    rootFrame.mainloop()


# url = 'https://nvna.eu/wp/';
# group = 62620113
# queryType = 'group'
# # Calculate current week on startup
# week = 41
# requestParameters = {'group':group, 'queryType':queryType, 'Week':week};
# request = requests.get(url, params=requestParameters);

# def browseFolder():
#     return;

# def export():
#     return request.text;