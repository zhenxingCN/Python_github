import logging

LOG_FILENAME='python_log.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug('This message should go to the log file')