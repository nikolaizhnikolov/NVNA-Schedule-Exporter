import requests;
from tkinter import *;
from tkinter import ttk;

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

    # Create parameter fields and labels
    # TODO:FUNCTIONALITY - go over each element and set its corresponding type and config
    # Group Number
    ttk.Label(mainFrame, text='Group').grid(column=0, row=0)
    group = IntVar()
    ttk.Entry(mainFrame, textvariable=group).grid(column=0, row=1)


    # Query Type
    ttk.Label(mainFrame, text='Type').grid(column=1, row=0)
    queryType = StringVar(rootFrame)
    queryType.set("Group") # default value
    OptionMenu(mainFrame, queryType, 'Group', 'Lecturer', 'Week').grid(column=1, row=1)
    # Week Number
    ttk.Label(mainFrame, text='Week').grid(column=2, row=0)
    ttk.Entry(mainFrame).grid(column=2, row=1)
    # Export functionality
    ttk.Label(mainFrame, text="Output folder:").grid(column=0, row=2)
    ttk.Button(mainFrame, text="Browse...").grid(column=1, row=2);
    ttk.Entry(mainFrame).grid(column=0, columnspan=2, row=3)
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