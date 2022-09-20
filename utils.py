import logging
from starlette_context import context


class RequestFilter(logging.Filter):
    def filter(self, record):
        if context.exists():
            record.request_id = context.data['X-Request-ID']
        else:
            record.request_id = ''
        return record


FORMAT = '%(asctime)s %(levelname)s [%(name)s] [%(request_id)s] [%(filename)s:%(lineno)d] - %(message)s'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()  # Logger
logger_handler = logging.StreamHandler()  # Handler for the logger
logger.addHandler(logger_handler)
logger_handler.setFormatter(logging.Formatter(FORMAT))
logger_handler.addFilter(RequestFilter())
