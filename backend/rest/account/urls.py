from django.urls import path
from .views import registration_view, validate_token, account_profile, update_account_profile
from rest_framework.authtoken.views import obtain_auth_token


app_name = "account"

urlpatterns = [
    path('validate', validate_token, name="validate"),
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('profile', account_profile, name="profile"),
    path('update', update_account_profile, name="update")
]