import re
import unicodedata
from datetime import datetime

import requests
from requests import RequestException
from requests.models import HTTPError

import ExporterLogger as logger
import ExporterUtil as util
import FileExporter

URL = 'https://nvna.eu/wp/'

WEEKDAYS = ['Понеделник',
            'Вторник',
            'Сряда',
            'Четвъртък',
            'Петък',
            'Събота',
            'Неделя']

FLAGS = re.IGNORECASE | re.UNICODE | re.MULTILINE | re.VERBOSE


def get_weekly_data(group, query_type, week):
    try:
        request_parameters = \
            {'group': group,
             'queryType': query_type.lower(),
             'Week': week}

        request = requests.put(URL, params=request_parameters, timeout=5)
        if request.status_code != requests.codes['ok']:
            raise HTTPError
        return(request.text)

    except RequestException as e:
        logger.error(e)


def sanitize_weekly_data(raw_data, month) -> list:
    # Create weekly list
    weekly_data = []
    for weekday in WEEKDAYS:
        # For each day of the week
        # Try no lectures first
        no_lecture_regex = re.compile(util.daily_regex_template(
            weekday, month) + util.no_lecture_regex_template())
        no_lecture = no_lecture_regex.search(raw_data)
        # If found then there were no lectures for that day
        if no_lecture is not None:
            daily_data = []
            daily_data.append(no_lecture.group(2))
            daily_data.append("Няма занятия")
            weekly_data.append(daily_data)
        # Else - get a regex for the whole day, then search it for any lecture
        # templates
        else:
            lectures_schedule_regex = re.compile(util.daily_regex_template(
                weekday, month) + util.daily_schedule_regex_template(), FLAGS)
            lectures_schedule = lectures_schedule_regex.search(raw_data)

            if lectures_schedule is not None:
                lectures_regex = re.compile(
                    util.lecture_regex_template(), FLAGS)
                lectures = lectures_regex.findall(lectures_schedule.group(0))
                if lectures.__len__ != 0:
                    daily_data = []
                    daily_data.append(lectures_schedule.group(2))
                    daily_data.append(lectures_schedule.group(3))
                    for lecture in lectures:
                        daily_data.append(str.strip(lecture[0]))
                        daily_data.append(str.strip(lecture[1]))
                        daily_data.append(str.strip(lecture[2]))
                        daily_data.append(str.strip(lecture[3]))
                        daily_data.append(
                            unicodedata.normalize(
                                "NFKD", lecture[4]))
                        if (lecture[5] is not None):
                            daily_data.append(str.strip(lecture[6]))
                    weekly_data.append(daily_data)
    return weekly_data


def extract_weekly_data(group, query_type, week):
    raw_data = get_weekly_data(group, query_type, week)
    return sanitize_weekly_data(raw_data, None)

def extract_monthly_data(group, query_type, week, month):
    raw_data = get_weekly_data(group, query_type, week)
    return sanitize_weekly_data(raw_data, month)

def export_monthly_data(
        group,
        query_type,
        month_name,
        output_folder,
        file_name):
    month_index = datetime.strptime(month_name, '%B').month
    weekly_indices = util.get_weekly_indices_for_month(month_name)

    # Create empty list to store daily results
    logger.info('Getting schedule for Month: ' + str(month_name))
    monthly_data = []
    for week_index in weekly_indices:
        logger.info('Getting schedule for Week: ' + str(week_index))
        # Add weekly data to monthly
        weekly_data = extract_monthly_data(
            group, query_type, week_index, month_index)
        for day_data in weekly_data:
            monthly_data.append(day_data)
            logger.info(day_data)

    # Export data
    return FileExporter.export_monthly_report(
        monthly_data,
        output_folder,
        file_name)

def export_weekly_data(
        group,
        query_type,
        first_week,
        last_week,
        output_folder,
        file_name,
        file_type):
    
    weekly_indices = range(first_week, last_week + 1)

    # Create empty list to store daily results
    logger.info('Getting schedule for Week range: ' + str(first_week) + ' to ' + str(last_week))
    data = []
    for week_index in weekly_indices:
        logger.info('Getting schedule for Week: ' + str(week_index))
        # Add weekly data to monthly
        weekly_data = extract_weekly_data(
            group, query_type, week_index)
        for day_data in weekly_data:
            data.append(day_data)
            logger.info(day_data)

    # Export data
    return FileExporter.export_simple_report(
        data,
        output_folder,
        file_name,
        file_type,
        weekly_indices)
