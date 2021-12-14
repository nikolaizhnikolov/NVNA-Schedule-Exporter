from datetime import date, datetime
from requests import RequestException
from requests.models import HTTPError
import calendar
import requests
import ExcelExporter
import re
import ExporterLogger as logger

url = 'https://nvna.eu/wp/'

weekdays = ['Понеделник',
            'Вторник',
            'Сряда',
            'Четвъртък',
            'Петък',
            'Събота',
            'Неделя']

flags =  re.IGNORECASE | re.UNICODE | re.MULTILINE | re.VERBOSE

class ExporterRequestErrorMessages:
    ConnectionErrorMessage = "A connection error has occured"
    TimeoutErrorMessage = "Request timeout. \
                           Requests stay idle for no more than 1 second \
                           of not receiving any packages!"
    HTTPErrorMessage = "Request not successful"
    RequestExceptionMessage = "There was an ambiguous exception that \
                               occurred while handling your request."

def get_weekly_data(group, query_type, week):
    try:
        request_parameters = \
            {'group':       group,
            'queryType':    query_type.lower(),
            'Week':         week}

        request = requests.put(url, params=request_parameters, timeout=1)
        if request.status_code != requests.codes['ok']:
            raise HTTPError
        return(request.text)
    
    except ConnectionError:
        logger.error(ExporterRequestErrorMessages.ConnectionErrorMessage)
    except HTTPError:
        logger.error(ExporterRequestErrorMessages.HTTPErrorMessage)
    except TimeoutError:
        logger.error(ExporterRequestErrorMessages.TimeoutErrorMessage)
    except RequestException:
        logger.error(ExporterRequestErrorMessages.RequestExceptionMessage)

def daily_regex_template(day, month):
    return '(<tr><td[^>]+>('+str(day)+',\s[0-9]{4}-[0]?'+str(month)+'-[0-9]{2})</td></tr>)'

def daily_schedule_regex_template():
    return '(<tr>(<td[^<]+</td>){1,5}</tr>){13}'

def no_lecture_regex_template():
    return '(<tr><td[^>]+>Няма занятия</td></tr>)'
    
def lecture_regex_template():
    return '''<tr>
                <td>([0-9])</td>
                <td[^>]*>([0-9]{1,2}:[0-9]{2}-[0-9]{1,2}:[0-9]{2})</td>
                <td[^>]*>([^<]*)</td>
                <td[^>]*>([^<]*)</td>
                <td[^>]*>([^<]*)</td>
            </tr>'''

def sanitize_weekly_data(raw_data, month) -> list:
    # Create weekly list
    weekly_data = []
    for weekday in weekdays:
        # For each day of the week
        # Try no lectures first
        no_lecture_regex = re.compile(daily_regex_template(weekday, month) + no_lecture_regex_template())
        no_lecture = no_lecture_regex.search(raw_data)
        # If found then there were no lectures for that day
        if no_lecture != None:
            weekly_data.append(no_lecture.group(2))       
        # Else - get a regex for the whole day, then search it for any lecture templates  
        else:
            lectures_schedule_regex = re.compile(daily_regex_template(weekday, month) + daily_schedule_regex_template(), flags)
            lectures_schedule = lectures_schedule_regex.search(raw_data)
            
            if lectures_schedule != None:
                lectures_regex = re.compile(lecture_regex_template(), flags)
                lectures = lectures_regex.findall(lectures_schedule.group(0))
                if lectures.__len__ != 0:
                    weekly_data.append(lectures_schedule.group(2));
                    for lecture in lectures:   
                        weekly_data.append("Начало: " + lecture[0]);
                        weekly_data.append("Продължителност: " + lecture[1]);
                        weekly_data.append("Лекция: " + str.strip(lecture[2]));
                        weekly_data.append("Място: " + lecture[3]);
                        weekly_data.append("Лектор: " + lecture[4]);
                        weekly_data.append("");
    return weekly_data

def extract_weekly_data(group, query_type, week, month):
    raw_data = get_weekly_data(group, query_type, week)
    return sanitize_weekly_data(raw_data, month)

def save_data_into_file(data):
    # TODO: save data into excel file instead of txt
    text_file = open("sample.txt", 'w', encoding='UTF-8')
    text_file.write(data)

def export_monthly_data(group, query_type, month_name, output_folder):
    # Get index of month for calculations
    month_index = datetime.strptime(month_name, '%B').month
    # The date we are calculating against is the first of the month
    export_date = date.today().replace(day=1, month=month_index)
    # We find the first week and the number of weeks
    first_week_index = export_date.isocalendar().week
    weeks_in_month = len(calendar.monthcalendar(export_date.year, export_date.month))
    weeks_in_month = range(weeks_in_month)
    # Create empty list to store daily results
    logger.info('Getting schedule for Month: ' + str(month_name))
    monthly_data_list = []
    for week in weeks_in_month:
        week_index = first_week_index + week
        logger.info('Getting schedule for Week: ' + str(week_index))
        # Add weekly data to monthly
        weekly_data = extract_weekly_data(group, query_type, week_index, month_index)
        for day_data in weekly_data:
            monthly_data_list.append(day_data)
    for day in monthly_data_list:
        logger.info(day);
    # export data into excel 
    ExcelExporter.export_data_into_excel("")
