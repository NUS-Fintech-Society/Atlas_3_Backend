from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return HttpResponse()
        else:
            return HttpResponseForbidden()
    return HttpResponse()


def logout(request):
    django_logout(request)
    return HttpResponse()


@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request):
    return HttpResponse()
