# =============================================================================
# ============================= ENUMS =========================================
# =============================================================================
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

EXPORT_TYPES = ['.xlsx',
                '.docx',
                '.txt']

class ExportTypes: 
    EXCEL=      '.xlsx'
    WORD=       '.docx'
    PLAINTEXT= '.txt'


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

def get_default_export_type():
    return ExportTypes.EXCEL

# =============================================================================
# ============================= REGEX TEMPLATES ===============================
# =============================================================================
def daily_regex_template(day, month):
    return '(<tr><td[^>]+>('+str(day)+',\s[0-9]{4}-[0]?'+str(month)+'-[0-9]{2})</td></tr>)'

def daily_schedule_regex_template():
    return '(<tr>(<td[^<]+</td>){1,6}</tr>){13}'

def no_lecture_regex_template():
    return '(<tr><td[^>]+>Няма занятия</td></tr>)'

# This regex works for groups and rooms, the last added conditional <td> 
# is required to make it work for lecturers as well
def lecture_regex_template():
    return '''<tr>
                <td>([0-9])</td>
                <td[^>]*>([0-9]{1,2}:[0-9]{2}-[0-9]{1,2}:[0-9]{2})</td>
                <td[^>]*>([^<]*)</td>
                <td[^>]*>([^<]*)</td>
                <td[^>]*>([^<]*)</td>
                (<td[^>]*>([^<]*)</td>)?
            </tr>'''
            