# -*- coding: utf-8 -*-

import sys
import logging
import threading
from typing import Callable

logger = logging.getLogger("errcallback")


class LoggingIntegration:
    def __init__(self, log_level: int):
        self.log_level = log_level

    def handle_logger(self, func: Callable):
        old_callHandlers = logging.Logger.callHandlers
        log_level = self.log_level

        def callHandlers(self, record):
            try:
                return old_callHandlers(self, record)
            finally:
                if func.__name__ == record.funcName or record.name == "errcallback":
                    return

                if record.levelno >= log_level:
                    func(record)

        logging.Logger.callHandlers = callHandlers


class ExceptHookIntegration:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        self.func(exc_type, exc_value, exc_traceback)

    def threading_handle_exception(self, exc):
        self.func(exc.exc_type, exc.exc_value, exc.exc_traceback)


def registry_err_callback(
        *, exception_func: Callable = None, logger_func: Callable = None, log_level: int = logging.ERROR):
    """registry error callack event

    Args:
        exception_func (Callable, optional): exception callback function. Defaults to None.
        logger_func (Callable, optional): logging callback function. Defaults to None.
        log_level (int, optional): logging callback level. Defaults to logging.ERROR.
    """
    if exception_func is not None:
        except_hook = ExceptHookIntegration(func=exception_func)
        sys.excepthook = except_hook.handle_exception
        threading.excepthook = except_hook.threading_handle_exception

    if logger_func is not None:
        LoggingIntegration(log_level=log_level).handle_logger(func=logger_func)
