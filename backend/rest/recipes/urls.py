from django.urls import path
from .views import RecipeAPIView, RecipeDetails

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view()),
    path('recipes/<int:id>', RecipeDetails.as_view())
]
