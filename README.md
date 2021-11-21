# err-callback-py
Python log error or exception callback

# install
```
pip install errcallback
```

# Usage
logging callback
```
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


# output
INFO:__main__:info test
ERROR:__main__:error test
INFO:__main__:callback func lineno: 17 message: error test
```

exception callback
```
import logging

from errcallback import registry_err_callback


def callback_func(exc_type, exc_value, exc_traceback):
    logging.error("callback_func>>>>>>>>>>>>>>", exc_info=(
        exc_type, exc_value, exc_traceback))


registry_err_callback(exception_func=callback_func)

1 / 0


# output
ERROR:root:callback_func>>>>>>>>>>>>>>
Traceback (most recent call last):
  File "examples/exception_demo.py", line 13, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

callback message to DingTalk, Email, Prometheus
```
...
from errcallback import registry_err_callback


def callback_func(exc_type, exc_value, exc_traceback):
    # todo send to DingTalk, Email, Prometheus


registry_err_callback(exception_func=callback_func)
...
```