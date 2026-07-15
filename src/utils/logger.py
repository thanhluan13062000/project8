import logging
import os


def get_logger(name,log_to_file = True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        os.makedirs("logs",exist_ok=True)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s |  %(name)-10s | %(message)s"
        )
        if log_to_file:
            file_handle = logging.FileHandler(f"logs/{name}.log")
            file_handle.setLevel(logging.INFO)
            file_handle.setFormatter(formatter)
            logger.addHandler(file_handle)
        console_handle = logging.StreamHandler()
        console_handle.setLevel(logging.INFO)
        console_handle.setFormatter(formatter)
        logger.addHandler(console_handle)
    return logger