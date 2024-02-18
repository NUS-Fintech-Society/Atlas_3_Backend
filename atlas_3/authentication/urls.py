from django.urls import path

from . import views


urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("csrf", views.get_csrf_token, name="csrf"),
]
