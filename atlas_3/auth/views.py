from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.http import HttpResponse, HttpResponseForbidden


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
