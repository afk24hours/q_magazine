# MIDDLEWARE TEST

class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(request.META['HTTP_USER_AGENT'])
        res = self.get_response(request)
        return res
