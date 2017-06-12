from logging.handlers import SysLogHandler
import logging

logger = logging.getLogger()
handler = logging.handlers.SysLogHandler(address = ('localhost',514), facility=19)
logger.addHandler(handler)

logging.warn("Hello world")
