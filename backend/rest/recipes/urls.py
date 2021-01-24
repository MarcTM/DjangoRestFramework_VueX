from django.urls import path
from .views import recipe_list, recipe_details

urlpatterns = [
    path('recipes/', recipe_list),
    path('recipes/<int:id>', recipe_details)
]
