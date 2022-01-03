from datetime import date
from genericpath import exists
import os
import ExporterLogger as logger
import ExporterUtil as util
import configparser

CWD = os.getcwd()
CONFIG_PATH = CWD + '\exporter_config.cfg'

logger.info("Current working directory set to:" + CWD)

config_parser = configparser.RawConfigParser()

def create_config():
    file_exists = exists(CONFIG_PATH)
    if not file_exists:
        file = open(CONFIG_PATH, 'w')
        file.close()
    config_parser.read(CWD+'\exporter_config.cfg', encoding='UTF-8')
    if not config_parser.has_section('request_parameters'):
        config_parser.add_section('request_parameters')
        

def update_config(group, query_type, month, export_directory, export_file_name):
    # Проверка за съществуване на файл и секция
    create_config()
    # Запаметяване на пареметри
    config_parser.set('request_parameters', 'group', group)
    config_parser.set('request_parameters', 'query_type', query_type)
    config_parser.set('request_parameters', 'month', month)
    config_parser.set('request_parameters', 'export_directory', export_directory)  
    config_parser.set('request_parameters', 'export_file_name', export_file_name)   
    
    with open(CWD+'\exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)     
        
# Първоначална проверка за файл       
create_config()

group=              config_parser.get('request_parameters', 'group', fallback='0')
query_type=         config_parser.get('request_parameters', 'query_type', fallback=util.get_default_interface_query_type())
month=              config_parser.get('request_parameters', 'month', fallback=util.get_interface_month(date.today().strftime('%B')))
export_directory=   config_parser.get('request_parameters', 'export_directory', fallback=CWD)
export_file_name=   config_parser.get('request_parameters', 'export_file_name', fallback="Export")
