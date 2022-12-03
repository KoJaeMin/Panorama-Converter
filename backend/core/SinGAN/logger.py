import logging
from datetime import datetime

def get_log_level(level : str) -> int:
    level_name = level.upper()
    log_level = ['DEBUG','INFO','WARNING','ERROR','CRITICAL']
    if level_name in log_level:
        return 10 * (log_level.index(level_name)+1)
    return 0

def get_log_format(level : int) -> object:
    if level > 20:
        return logging.Formatter('[%(levelname)s:%(name)s:%(asctime)s] %(message)s')
    return logging.Formatter('%(processName)s/%(process)d-[%(levelname)s:%(asctime)s] %(message)s')

def custom_logger(name : str, level : str = 'DEBUG', file_directory : str = './') -> None:
    logger = logging.getLogger(name)
    date = datetime.today().strftime("%Y_%m_%d")

    log_level = get_log_level(level)
    formatter = get_log_format(log_level)
    file_handler = logging.FileHandler(filename=f"{file_directory}[{date}]{log_level}_log.log")
    
    logger.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

if __name__ == '__main__':
    cl = custom_logger("test",'INFO')
    cl.info("test")
    