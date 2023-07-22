from django.utils import timezone
from .models import RequestResponseLog

class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = timezone.now()

        response = self.get_response(request)

        end_time = timezone.now()
        elapsed_time = (end_time - start_time).microseconds // 1000

        path = request.path
        request_method = request.method

        RequestResponseLog.objects.create(
            path=path,
            request_method=request_method,
            time=elapsed_time
        )

        return response
