import logging

from errcallback import registry_err_callback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def callback_func(record):
    logger.info("callback func lineno: %s message: %s",
                record.lineno, record.message)


registry_err_callback(logger_func=callback_func, log_level=logging.ERROR)

logger.info("info test")
logger.error("error test")
