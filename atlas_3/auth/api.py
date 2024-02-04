from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from ninja import Router
from ninja.security import django_auth

router = Router()


@router.get("/private_data", auth=django_auth)
def private_data(request):
    return {"data": "Private data"}


@router.post("/csrf")
@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request):
    return HttpResponse()
