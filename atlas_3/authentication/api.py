from ninja import Router
from ninja.security import django_auth

from .models import AtlasUser

router = Router()


@router.get("/private_data", auth=django_auth)
def private_data(request):
    return {"data": "Private data"}


@router.post("/user", auth=django_auth)
def get_user(request):
    atlas_user = request.user.atlasuser
    return {
        "username": request.user.username,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "profile_picture": atlas_user.profile_picture.url,
        "department": atlas_user.department,
        "role": atlas_user.role,
        "telegram_handle": atlas_user.telegram_handle,
    }
