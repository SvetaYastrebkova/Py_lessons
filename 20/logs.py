from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import pathlib
import sys


# Logging levels:
"""
Level	    When it’s used

NOT_SET     = WARNING
DEBUG	    Подробная информация, обычно представляющая интерес только при диагностике проблем.
INFO	    Подтверждение того, что все работает так, как ожидалось.
WARNING	    Указание на то, что произошло что-то неожиданное, или указание на какую-то проблему в ближайшем будущем (например, «недостаточно места на диске»). Программное обеспечение по-прежнему работает, как ожидалось.
ERROR	    Из-за более серьезной проблемы программное обеспечение не может выполнять некоторые функции.
CRITICAL	Серьезная ошибка, указывающая на то, что сама программа не может продолжать работу.
"""

LOG_FILE = pathlib.Path(__file__).parent.joinpath('test_custom_log1.log')
LOG_LEVEL = logging.DEBUG
FILE_MODE = 'a' # Default mode

# create custom logger
## file handler
my_file_handler = RotatingFileHandler(
    filename=LOG_FILE,
    mode=FILE_MODE,
    maxBytes=600,
    backupCount=3
)
my_file_handler.setLevel(LOG_LEVEL)
def custom_namer(default_name):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{default_name}.{timestamp}.bak"
my_file_handler.namer = custom_namer

## formatter
my_formatter = logging.Formatter('%(asctime)-20s, %(levelname)-10s, %(message)-s')
my_file_handler.setFormatter(my_formatter)

## create logger
my_logger = logging.getLogger()
my_logger.addHandler(my_file_handler)

# create console logger
console_logger = logging.getLogger()
console_logger.setLevel(logging.ERROR)
console_logger.addHandler(logging.StreamHandler(sys.stdout))


# write messages to my_logger
my_logger.debug("This is DEBUG type message")
my_logger.info("This is INFO type message")
my_logger.warning("This is warning type message")
my_logger.error("This is error type message")
my_logger.critical("This is critical type message")

# write messages to console_logger
console_logger.debug("This is DEBUG type message")
console_logger.info("This is INFO type message")
console_logger.warning("This is is warning type message")
console_logger.error("This is error type message")
console_logger.critical("This is critical type message")

