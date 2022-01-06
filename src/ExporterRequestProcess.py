from datetime import date, datetime
from requests import RequestException
from requests.models import HTTPError
import calendar
import requests
import ExcelExporter
import re
import unicodedata
import ExporterLogger as logger
import ExporterUtil as util

URL = 'https://nvna.eu/wp/'

WEEKDAYS = ['Понеделник',
            'Вторник',
            'Сряда',
            'Четвъртък',
            'Петък',
            'Събота',
            'Неделя']

FLAGS =  re.IGNORECASE | re.UNICODE | re.MULTILINE | re.VERBOSE

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

        request = requests.put(URL, params=request_parameters, timeout=5)
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

def sanitize_weekly_data(raw_data, month) -> list:
    # Create weekly list
    weekly_data = []
    for weekday in WEEKDAYS:
        # For each day of the week
        # Try no lectures first
        no_lecture_regex = re.compile(util.daily_regex_template(weekday, month) + util.no_lecture_regex_template())
        no_lecture = no_lecture_regex.search(raw_data)
        # If found then there were no lectures for that day
        if no_lecture != None:
            daily_data = []
            daily_data.append(no_lecture.group(2));
            daily_data.append("Няма занятия")
            weekly_data.append(daily_data)       
        # Else - get a regex for the whole day, then search it for any lecture templates  
        else:
            lectures_schedule_regex = re.compile(util.daily_regex_template(weekday, month) + util.daily_schedule_regex_template(), FLAGS)
            lectures_schedule = lectures_schedule_regex.search(raw_data)
            
            if lectures_schedule != None:
                lectures_regex = re.compile(util.lecture_regex_template(), FLAGS)
                lectures = lectures_regex.findall(lectures_schedule.group(0))
                if lectures.__len__ != 0:
                    daily_data = []
                    daily_data.append(lectures_schedule.group(2));
                    for lecture in lectures:   
                        daily_data.append(lecture[0])
                        daily_data.append(lecture[1])
                        daily_data.append(str.strip(lecture[2]))
                        daily_data.append(lecture[3])
                        daily_data.append(unicodedata.normalize("NFKD", lecture[4]))
                        if (lecture[5] is not None):
                            daily_data.append(lecture[6])
                    weekly_data.append(daily_data)
    return weekly_data

def extract_weekly_data(group, query_type, week, month):
    raw_data = get_weekly_data(group, query_type, week)
    return sanitize_weekly_data(raw_data, month)

def export_monthly_data(group, query_type, month_name, output_folder, file_name):
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
            logger.info(day_data)
            
    # Export data into excel file
    return ExcelExporter.export_data_into_excel(monthly_data_list, month_name, output_folder, file_name)
