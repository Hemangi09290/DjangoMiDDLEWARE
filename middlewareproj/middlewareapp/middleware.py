import logging

logger = logging.getLogger(__name__)
class RequestLogger1:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info("BEFORE RequestLogger1")
        print("BEFORE RequestLogger1")
        response = self.get_response(request)
        logger.info("AFTER RequestLogger1")
        print("AFTER RequestLogger1")
        logger.info(f"method={request.method} path={request.path}")
        return response
        
class RequestLogger2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("BEFORE RequestLogger2")
        response = self.get_response(request)
        print("AFTER RequestLogger1")
        return response