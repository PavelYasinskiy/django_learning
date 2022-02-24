import datetime

class Log:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.get_full_path()
        if request.is_secure() is True:
            http = 'https'
        else:
            http = "http"
        log_time = datetime.datetime.now()
        log = f"URL: {url} | HTTP-METHOD: {http}  | time: {log_time} \n"
        with open("logging.log", "a") as logging:
            logging.write(log)

        response = self.get_response(request)

        return response