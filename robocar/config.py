import os
import logging

# Robocar location, don't change this:
SRC_DIR = os.path.dirname(os.path.realpath(__file__))

# Logging
LOGGING_LEVEL = logging.INFO # Minimum level for logging messages stored in logs
LOGGING_FORMAT = '%(asctime)-10s ROBOCAR-V0 |%(levelname)s: %(message)s' # Log message format
LOGGING_DATE_FORMAT = '%d %H:%M:%S' # Log message date format
LOGGING_BACKUP_COUNT = 3 # Number of log files
LOG_FILE_MAX_BYTES = 6000 # Max bytes per log file
LOGS_DIR = '/home/pi/car_logs' # Where to keep logs