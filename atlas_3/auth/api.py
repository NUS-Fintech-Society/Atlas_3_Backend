from django.contrib.auth import authenticate, login as django_login

from ninja import Router
from ninja.security import django_auth

router = Router()


@router.get("/private_data", auth=django_auth)
def private_data(request):
    return {"data": "Private data"}
