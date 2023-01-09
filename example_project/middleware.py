from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):
    pass
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("Processing {view_func}".format(view_func=view_func))
    #     view_kwargs['a'] = 10
    #     return view_func(request, *view_args, **view_kwargs)

    # def process_exception(self, request, exception):
    #     return HttpResponse('exception')
        # return None

    # def process_request(self, request):
    #     request.GET = {}
    #     request.GET['b'] = 10

    # def process_response(self, request, response):
    #     print(response)
    #
    #     return response