import datetime
from time import time

from teachers.models import Logger


class LogMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        rpath = request.path.split('/')
        if rpath[1] == 'admin':
            now = datetime.datetime.now()
            Logger.objects.create(path=request.path,
                                  method=request.method,
                                  execution_time=end-start,
                                  created=str(now))
        return response
