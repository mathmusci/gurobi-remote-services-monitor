import os
import inspect
import logging
import uuid

from logging.handlers import RotatingFileHandler

LOGGING_DEBUG_LEVEL = os.getenv("LOGGING_LEVEL", default="DEBUG")  # possible options: "DEBUG", "INFO", "WARNING", "ERROR", and "CRITICAL"
LOGGING_FILENAME = os.getenv("LOGGING_FILENAME", default="log.txt")
LOGGING_BACKUP_COUNT = 5
LOGGING_MAX_BYTES = 20 * 1024 * 1024


def set_logging(debug_level=LOGGING_DEBUG_LEVEL, log_filename=LOGGING_FILENAME, announce_initialisation = False):
    """
    Set the format of logging, output filename and debug level.

    Input arguments:

    debug_level :: possible values are 'DEBUG'/'debug', 'INFO'/'info', 'WARNING'/'warning', 
                   'ERROR'/'error', 'CRITICAL'/'critical'. If debug_level is of an unknown type, 'DEBUG' is used.

    log_filename :: the name of the log file to be used by logging.

    announce_initialisation :: if set to True, a confirmation message will be output into log_filename.
    """

    logger = logging.getLogger("grb_rs_monitor")

    if not debug_level.lower() in {"debug", "info", "warning", "error", "critical"}:
        debug_level = "debug"

    logging.basicConfig(
        filename=log_filename,
        format="%(asctime)s - %(name)s - [%(levelname)s] %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
        level=logging.__dict__[debug_level.upper()])
        
    logger.addHandler(RotatingFileHandler(log_filename, maxBytes=LOGGING_MAX_BYTES, backupCount=LOGGING_BACKUP_COUNT))

    if announce_initialisation: 
        msg = "Logging is set up now - using logging level {}".format(logging.__dict__[debug_level.upper()])
        logger.debug(msg)   
    return logger

logger = set_logging()

def log_this(logger=logger, input_args_dump=False):
    def log_this_decorator(func):
        def func_wrapper(*args, **kwargs):
            r = inspect.stack()
            parents_name = r[1][1]
            unique_uuid = uuid.uuid4().hex.upper()

            # log START OF CALL
            logger.info("{}:{} #{} CALL".format(parents_name, func.__name__, unique_uuid))

            if input_args_dump:
                # log both positional and optional argument names and argument values
                args_name = inspect.getargspec(func)[0]
                args_dict = dict(zip(args_name, args))
                for arg in args_dict:
                    logger.debug("input (positional) argument {}={}".format(arg, args_dict[arg]))
                for arg in kwargs:
                    logger.debug("input (optional) argument {}={}".format(arg, kwargs[arg]))

            # proceed with executing the function
            res = func(*args, **kwargs)

            # log END OF CALL
            logger.info("{}:{} #{} END OF CALL".format(parents_name, func.__name__, unique_uuid))
            return res

        func_wrapper.__name__ = func.__name__
        func_wrapper.__doc__ = func.__doc__
        return func_wrapper

    return log_this_decorator
