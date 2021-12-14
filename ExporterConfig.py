from datetime import date
from genericpath import exists
import os
import ExporterLogger as logger
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
        

def update_config(group, query_type, month, export_directory):    
    create_config()
    # Save request parameters into cfg for next use
    config_parser.set('request_parameters', 'group', group)
    config_parser.set('request_parameters', 'query_type', query_type)
    config_parser.set('request_parameters', 'month', month)
    config_parser.set('request_parameters', 'export_directory', export_directory)    
    
    with open(CWD+'\exporter_config.cfg', 'w', encoding='UTF-8') as config_file:
        config_parser.write(config_file)     
        
        
create_config()

group=              config_parser.get('request_parameters', 'group', fallback='0')
query_type=         config_parser.get('request_parameters', 'query_type', fallback='Group')
month=              config_parser.get('request_parameters', 'month', fallback=date.today().strftime('%B'))
export_directory=   config_parser.get('request_parameters', 'export_directory', fallback=CWD)
