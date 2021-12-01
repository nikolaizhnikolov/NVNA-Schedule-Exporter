from datetime import date, datetime, time
import requests
import ExcelExporter
from requests import RequestException
from requests.models import HTTPError
from requests.sessions import Request;

url = 'https://nvna.eu/wp/'

class ExporterRequestErrorMessages:
    ConnectionErrorMessage = "A connection error has occured"
    TimeoutErrorMessage = "Request timeout. Requests stay idle for no mor than 1 second of not receiving any packages!"
    HTTPErrorMessage = ""
    RequestExceptionMessage = ""


def get_weekly_data(group, query_type, week):
    try:
        request_parameters = \
            {'group':       group,
            'queryType':    query_type.lower(),
            'Week':         week}

        request = requests.put(url, params=request_parameters, timeout=1)
        if request.status_code != requests.codes['ok']:
            raise HTTPError
        else:
            extract__weekly_data(request.text)

    except ConnectionError:
        return ExporterRequestErrorMessages.ConnectionErrorMessage
    except HTTPError:
        return ExporterRequestErrorMessages.HTTPErrorMessage
    except TimeoutError:
        return ExporterRequestErrorMessages.TimeoutErrorMessage
    except RequestException:
        return ExporterRequestErrorMessages.RequestExceptionMessage    
    
def extract__weekly_data(group, query_type, week):
    return
    # print(request_text)
    
def save_data_into_file(data):
    # TODO: save data into excel file instead of txt
    text_file = open("sample.txt", 'w', encoding='UTF-8');
    text_file.write(data)


    
def export_monthly_data(group, query_type, month, output_folder):
    # TODO: weeks_array = Calculate week numbers for this month
    # for week : weeks_array
        # export_weekly_data(group, query_type, week)
    # sanitize days outsize of month range using a regex - (понеделник | вторник...) "[0-9]{4}-[month]-[0-9]{2}"
    # export data into excel 
    ExcelExporter.export_data_into_excel(request_text)

    return

