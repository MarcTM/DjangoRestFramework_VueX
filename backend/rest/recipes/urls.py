from django.urls import path, include
from .views import GenericAPIView, DetailsAPIView, RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('api/', include(router.urls)),

    path('recipes/', GenericAPIView.as_view()),
    path('recipes/<int:id>', DetailsAPIView.as_view())
]