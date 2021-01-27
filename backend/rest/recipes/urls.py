from django.urls import path, include
from .views import GenericAPIView, DetailsAPIView, RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('views', include(router.urls)),

    path('', GenericAPIView.as_view()),
    path('<int:id>', DetailsAPIView.as_view())
]