from django.http import HttpResponseRedirect,HttpResponse, HttpResponseForbidden


class AuthenticationRequired:
    def __init__(self, view_func):
        self.view_func = view_func

    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Authentication required")


@AuthenticationRequired
def test_view(request):
    return HttpResponse('this is test view')