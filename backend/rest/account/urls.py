from django.urls import path
from .views import registration_view, validate_token, account_profile, update_account_profile, get_cart, account_cart
from rest_framework.authtoken.views import obtain_auth_token


app_name = "account"

urlpatterns = [
    path('validate', validate_token, name="validate"),
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('profile', account_profile, name="profile"),
    path('cart', get_cart, name="cart"),
    path('cart/<int:id>', account_cart, name="account_cart"),
    path('update', update_account_profile, name="update")
]