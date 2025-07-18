import logging
from logging.handlers import RotatingFileHandler


def setup_logger(logger_name):
    # Create a logger instance
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Create a RotatingFileHandler to write logs to events.log with size limit
    file_handler = RotatingFileHandler(
        './events.log', maxBytes=20*1024*1024, backupCount=7
    )
    file_handler.setLevel(logging.DEBUG)

    # Create a Formatter to specify the log message format
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s in %(funcName)s:%(message)s")

    # Set the Formatter for the FileHandler
    file_handler.setFormatter(formatter)

    # Add the FileHandler to the logger
    logger.addHandler(file_handler)

    return logger
