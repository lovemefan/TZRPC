# -*- coding:utf-8 -*-
# @FileName  :logger.py
# @Time      :2023/7/26 09:42
# @Author    :lovemefan
# @Email     :lovemefan@outlook.com
import logging
import logging.handlers
import os
import sys

loggers_dict = {}
LEVEL = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
DEFAULT_LOG_FILE_DIR = "~/.cache/tzrpc-log/"
LOCAL_DEFAULT_LOG_FILE_DIR = os.path.join(
    os.getenv("LOCAL_DEFAULT_PATH", DEFAULT_LOG_FILE_DIR), "log"
)
DEFAULT_FILEHANDLER_FORMAT = (
    "[%(levelname)s] %(asctime)s " "[%(pathname)s:%(lineno)d] %(funcName)s: %(message)s"
)
DEFAULT_STDOUT_FORMAT = (
    "%(asctime)s - %(name)s - %(levelname)s - ["
    "%(filename)s:%(lineno)d] %(funcName)s: - %(message)s"
)
DEFAULT_REDIRECT_FILE_NAME = "tzrpc.log"


def _convert_level(level: str) -> int:
    """Convert the format of the log to logging level.

    Args:
        level (str): User log level.

    Returns:
        level (str): Logging level.
    """
    level_convert = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    level = level_convert.get(level, logging.INFO)

    return level


def get_logger(logger_name: str = "tzrpc", **kwargs) -> logging.Logger:
    """Get the logger. Both computing centers and bare metal servers are
    available.

    Args:
        logger_name (str): Logger name.
        kwargs (dict): Other input.
            to_std (bool): If set to True, output the log to stdout.
            save_log_file (bool): If set to false, output will not write a log file.
            stdout_level (str): The level of the log output to stdout.
                If the type is str, the options are DEBUG, INFO, WARNING, ERROR, CRITICAL.
            stdout_format (str): Log format.
            file_level (list[str] or tuple[str]): The level of the log output to file.
                eg: ['INFO', 'ERROR'] Indicates that the logger will output logs above
                    the level INFO and ERROR in the list to the corresponding file.
                The length of the list needs to be the same as the length of file_name.
            file_save_dir (str): The folder where the log files are stored.
            file_name (list[str] or list[tuple]): Store a list of output file names.
            max_file_size (int): The maximum size of a single log file. Unit: MB.
            max_num_of_files (int): The maximum number of files to save.

    Returns:
        logger (logging.Logger): Logger.
    """

    if logger_name in loggers_dict:
        return loggers_dict[logger_name]
    mf_logger = logging.getLogger(logger_name)

    save_log_file = kwargs.get("save_log_file", True)
    stdout_level = kwargs.get("stdout_level", "INFO")
    stdout_format = kwargs.get("stdout_format", "")
    file_level = kwargs.get("file_level", ("INFO", "ERROR"))
    file_save_dir = kwargs.get("file_save_dir", "")
    file_name = kwargs.get("file_name", ("info.log", "error.log"))
    max_file_size = kwargs.get("max_file_size", 50)
    max_num_of_files = kwargs.get("max_num_of_files", 5)

    to_std = kwargs.get("to_std", True)
    if to_std:
        if not stdout_format:
            stdout_format = DEFAULT_STDOUT_FORMAT
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(_convert_level(stdout_level))
        stream_formatter = logging.Formatter(stdout_format)
        stream_handler.setFormatter(stream_formatter)
        mf_logger.addHandler(stream_handler)

    logging_level = []
    for level in file_level:
        logging_level.append(_convert_level(level))

    if save_log_file:
        if not file_save_dir:
            file_save_dir = os.path.join(LOCAL_DEFAULT_LOG_FILE_DIR, "log")

        file_path = []
        for name in file_name:
            path = os.path.join(file_save_dir, name)
            path = os.path.realpath(path)
            base_dir = os.path.dirname(path)
            if not os.path.exists(base_dir):
                os.makedirs(base_dir, exist_ok=True)
            file_path.append(path)

        max_file_size = max_file_size * 1024 * 1024

        file_formatter = logging.Formatter(DEFAULT_FILEHANDLER_FORMAT)
        for i, level in enumerate(file_level):
            file_handler = logging.handlers.RotatingFileHandler(
                filename=file_path[i],
                maxBytes=max_file_size,
                backupCount=max_num_of_files,
            )
            file_handler.setLevel(level)
            file_handler.setFormatter(file_formatter)
            mf_logger.addHandler(file_handler)

    mf_logger.propagate = False
    mf_logger.parent = None

    loggers_dict[logger_name] = mf_logger

    return mf_logger
