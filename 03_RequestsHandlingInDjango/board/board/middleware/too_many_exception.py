from django.core.cache import cache
from django.core.exceptions import PermissionDenied

class TooMany:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        count = cache.get_or_set(f'{ip}', 0, 1)
        count += 1
        if count > 13:
            pass
            # raise PermissionDenied
        else:
            cache.set(f'{ip}', count, 1)
        response = self.get_response(request)

        return response