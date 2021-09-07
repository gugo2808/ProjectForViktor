from .views import check_password
from django.urls import path

urlpatterns = [
    path("accounts/login/", check_password)
]
