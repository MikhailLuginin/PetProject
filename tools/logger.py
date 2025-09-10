import coloredlogs
import logging
from pathlib import Path

formatters = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s  - %(message)s")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_ROOT / "my_logs.log"


def get_file_handler():
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatters)
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatters)
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    coloredlogs.install(level=logging.DEBUG, logger=logger, fmt="%(asctime)s - %(levelname)s - %(name)s  - %(message)s")
    return logger
