import logging
from logging.handlers import RotatingFileHandler
import os
import config as cfg

if not os.path.isdir(cfg.LOGS_DIR):
    os.mkdir(cfg.LOGS_DIR)

_logging_formatter = logging.Formatter(cfg.LOGGING_FORMAT, cfg.LOGGING_DATE_FORMAT)

_logging_sh = logging.StreamHandler()
_logging_sh.setLevel(logging.DEBUG)
_logging_sh.setFormatter(_logging_formatter)

_logging_rfh = RotatingFileHandler(cfg.LOGS_DIR + '/robocar.log', maxBytes=cfg.LOG_FILE_MAX_BYTES, backupCount=cfg.LOGGING_BACKUP_COUNT)
_logging_rfh.setLevel(cfg.LOGGING_LEVEL)
_logging_rfh.setFormatter(_logging_formatter)

logger = logging.getLogger("robocar-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(_logging_sh)
logger.addHandler(_logging_rfh)