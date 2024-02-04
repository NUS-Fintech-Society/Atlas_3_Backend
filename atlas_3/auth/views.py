from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST


@require_POST
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return HttpResponse()
    else:
        return HttpResponseForbidden()


@require_POST
def logout(request):
    django_logout(request)
    return HttpResponse()
