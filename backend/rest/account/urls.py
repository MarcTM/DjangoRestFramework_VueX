from django.urls import path
from account.views import registration_view, validate_token
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserAPIView


app_name = "account"

urlpatterns = [
    path('validate', validate_token, name="validate"),
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('<str:username>', UserAPIView.as_view())
]