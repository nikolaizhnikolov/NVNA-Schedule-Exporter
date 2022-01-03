
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

def get_query_type(interface_type):
    return QUERY_TYPES[INTERFACE_QUERY_TYPES.index(interface_type)]

def get_interface_query_type(type):
    return INTERFACE_QUERY_TYPES[QUERY_TYPES.index(type)]

def get_default_interface_query_type():
    return INTERFACE_QUERY_TYPES[1]

def get_month(interface_month):
    return MONTHS[INTERFACE_MONTHS.index(interface_month)]

def get_interface_month(month):
    return INTERFACE_MONTHS[MONTHS.index(month)]