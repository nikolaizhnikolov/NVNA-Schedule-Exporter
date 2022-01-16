from datetime import date, datetime
from genericpath import exists
import os
import ExporterLogger as logger
import ExporterUtil as util
import configparser

# CWD is relative to the source files
CWD = os.path.dirname(os.path.realpath(__file__))  # os.getcwd()
CWD = CWD.removesuffix(r'\src')
print('CWD is: ' + CWD)
CONFIG_PATH = CWD + '\\exporter_config.cfg'

logger.info("Current working directory set to:" + CWD)

config_parser = configparser.RawConfigParser()


def create_config():
    file_exists = exists(CONFIG_PATH)
    if not file_exists:
        file = open(CONFIG_PATH, 'w')
        file.close()
    config_parser.read(CWD + '\\exporter_config.cfg', encoding='UTF-8')
    if not config_parser.has_section('request_parameters'):
        config_parser.add_section('request_parameters')


def update_config(
        group,
        query_type,
        month,
        export_directory,
        export_file_name,
        export_file_type):
    # Check file and section exist
    create_config()
    # Set parameters
    config_parser.set('request_parameters', 'group', group)
    config_parser.set('request_parameters', 'query_type', query_type)
    config_parser.set('request_parameters', 'month', month)
    config_parser.set(
        'request_parameters',
        'export_directory',
        export_directory)
    config_parser.set(
        'request_parameters',
        'export_file_name',
        export_file_name)
    config_parser.set(
        'request_parameters',
        'export_file_type',
        export_file_type)
    # Re/write into config file
    with open(CWD + '\\exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)


# Initial file check
create_config()

group = config_parser.get('request_parameters', 'group', fallback='0')
query_type = config_parser.get(
    'request_parameters',
    'query_type',
    fallback=util.get_default_interface_query_type())
month = config_parser.get(
    'request_parameters',
    'month',
    fallback=util.get_interface_month(
        date.today().strftime('%B')))
export_directory = config_parser.get(
    'request_parameters',
    'export_directory',
    fallback=CWD)
export_file_name = config_parser.get(
    'request_parameters',
    'export_file_name',
    fallback="Export")
export_file_type = config_parser.get(
    'request_parameters',
    'export_file_type',
    fallback=util.get_default_export_type())
year = config_parser.get(
    'request_parameters',
    'year',
    fallback=datetime.today().year)
