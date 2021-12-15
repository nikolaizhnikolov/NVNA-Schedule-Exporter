import logging
import logging.handlers as handlers

logging.basicConfig(encoding='UTF-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = handlers.RotatingFileHandler('excel_exporter.log', mode='w', backupCount=9, encoding='UTF-8')
handler.setFormatter(formatter)

logger = logging.getLogger("excel_exporter")
logger.info("Starting up exporter interface...")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def info(message):
    logger.info(message)

def error(message):
    logger.error(message)