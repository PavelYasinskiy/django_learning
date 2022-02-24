from django.core.cache import cache
import time

class WaitSomeTime:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        count = int(cache.get_or_set(f'{ip}', 0))
        count += 1
        if count % 3 == 0:
            time.sleep(5)

        cache.set(f'{ip}', count)
        response = self.get_response(request)

        return response
