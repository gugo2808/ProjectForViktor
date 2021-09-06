from .views import check_password
from django.urls import path

urlpatterns = [
    path("login/", check_password)
]
