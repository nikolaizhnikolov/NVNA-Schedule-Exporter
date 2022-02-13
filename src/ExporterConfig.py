from datetime import date, datetime
from distutils.command.config import config
from genericpath import exists
from multipledispatch import dispatch
import os
import sys
import ExporterLogger as logger
import ExporterUtil as util
import configparser

# Determine if application is run as a script or .exe
if getattr(sys, 'frozen', False):
    CWD = os.path.dirname(sys.executable)
elif __file__:
    CWD = os.path.dirname(__file__)

logger.info("Current working directory set to:" + CWD)

CONFIG_PATH = CWD + '\\exporter_config.cfg'


config_parser = configparser.RawConfigParser()


def create_config():
    if not exists(CONFIG_PATH):
        file = open(CONFIG_PATH, 'w')
        file.close()
    config_parser.read(CWD + '\\exporter_config.cfg', encoding='UTF-8')
    if not config_parser.has_section('request_parameters'):
        config_parser.add_section('request_parameters')


def get(name, fallback):
    value = config_parser.get('request_parameters', name, fallback=fallback)
    logger.info("Getting " + name + " with value: " + str(value))
    return value


def set(name, value):
    logger.info("Setting " + name + " with new value: " + str(value))
    config_parser.set('request_parameters', name, value)


@dispatch(int, str, str, str, str)
def update_config(
        group,
        query_type,
        month,
        export_directory,
        export_file_name):
    # Check file and section exist
    create_config()

    logger.info("Updating configuration...")
    # Set parameters
    set('group', group)
    set('query_type', query_type)
    set('month', month)
    set('export_directory', export_directory)
    set('export_file_name', export_file_name)

    # Re/write into config file
    with open(CWD + '\\exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)
    logger.info("Finished updating...")


@dispatch(int, str, int, int, str, str, str)
def update_config(
        group,
        query_type,
        first_week,
        last_week,
        export_directory,
        export_file_name,
        export_file_type):
    # Check file and section exist
    create_config()

    # Set parameters
    set('group', group)
    set('query_type', query_type)
    set('first_week', first_week)
    set('last_week', last_week)
    set('export_directory', export_directory)
    set('export_file_name', export_file_name)
    set('export_file_type', export_file_type)

    # Re/write into config file
    with open(CWD + '\\exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)


# Initial file check
create_config()

group =             get('group', '0')
query_type =        get('query_type', util.get_default_interface_query_type())
month =             get('month', util.get_interface_month(date.today().strftime('%B')))
export_directory =  get('export_directory', CWD)
export_file_name =  get('export_file_name', "Export")
export_file_type =  get('export_file_type', util.get_default_export_type())
year =              get('year', datetime.today().year)
first_week =        get('first_week', 1)
last_week =         get('last_week', 2)
