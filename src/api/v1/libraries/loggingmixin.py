import logging

# logger_handler = "django"
logger_handler = "testing_v1"
class LoggingMixin(object):
    """
    Provides full logging of requests and responses
    """
    def __init__(self):
        self.logger = logging.getLogger(logger_handler)

    def initial(self, request, *args, **kwargs):
        self.logger = logging.getLogger(logger_handler)
        try:
            if "demod" in request.path or "comparison" in request.path:
                self.logger.debug({"method": request.method, "endpoint": request.path})
            else:
                self.logger.debug({"request": request.data, "method": request.method, "endpoint": request.path})
        except:
            self.logger.debug({"request": dict(), "method": request.method, "endpoint": request.path})
        super(LoggingMixin, self).initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        self.logger = logging.getLogger(logger_handler)
        if response:
            self.logger.debug(response.data)
        return super(LoggingMixin, self).finalize_response(request, response, *args, **kwargs)


