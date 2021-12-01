from datetime import date, datetime, time
from requests import RequestException
from requests.models import HTTPError
from requests.sessions import Request
import calendar
import requests
import ExcelExporter

url = 'https://nvna.eu/wp/'

class ExporterRequestErrorMessages:
    ConnectionErrorMessage = "A connection error has occured"
    TimeoutErrorMessage = "Request timeout. \
        Requests stay idle for no more than 1 second \
        of not receiving any packages!"
    HTTPErrorMessage = ""
    RequestExceptionMessage = ""


def get_weekly_data(group, query_type, week):
    try:
        request_parameters = \
            {'group':       group,
            'queryType':    query_type.lower(),
            'Week':         week}

        request = requests.put(url, params=request_parameters, timeout=1)
        extract__weekly_data(request.text)
        if request.status_code != requests.codes['ok']:
            raise HTTPError

    except ConnectionError:
        return ExporterRequestErrorMessages.ConnectionErrorMessage
    except HTTPError:
        return ExporterRequestErrorMessages.HTTPErrorMessage
    except TimeoutError:
        return ExporterRequestErrorMessages.TimeoutErrorMessage
    except RequestException:
        return ExporterRequestErrorMessages.RequestExceptionMessage

def extract_weekly_schedule(raw_data):
    # extract schedule from raw data by regex
    return

def extract__weekly_data(group, query_type, week):
    raw_data = get_weekly_data(group, query_type, week)
    return extract_weekly_schedule(raw_data)

def save_data_into_file(data):
    # TODO: save data into excel file instead of txt
    text_file = open("sample.txt", 'w', encoding='UTF-8')
    text_file.write(data)

def export_monthly_data(group, query_type, month_name, output_folder):
    # Get index of month for calculations
    month_index = datetime.strptime(month_name, '%B').month
    # The date we are calculating against is the first of the month
    export_date = date.today().replace(day=1, month=month_index)
    # We find the number of weeks and the first week
    week_index = export_date.isocalendar().week
    week_number = len(calendar.month(export_date.year, export_date.month))
    print(month_name + " Index: " + str(export_date.month))
    print("Starting week: " + str(week_index) + ", Weeks number: " + str(week_number))
    # Then we get the data for each of them
    # for week : weeks_array
        # export_weekly_data(group, query_type, week)
    # sanitize days outsize of month range using a regex - (понеделник | вторник...) "[0-9]{4}-[month]-[0-9]{2}"
    # export data into excel 
    ExcelExporter.export_data_into_excel("")
