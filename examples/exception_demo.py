import logging

from errcallback import registry_err_callback


def callback_func(exc_type, exc_value, exc_traceback):
    logging.error("callback_func>>>>>>>>>>>>>>", exc_info=(
        exc_type, exc_value, exc_traceback))


registry_err_callback(exception_func=callback_func)

1 / 0
