from django.urls import path, include
from .views import GenericAPIView, DetailsAPIView, ApiMealListView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', ApiMealListView.as_view()),
    path('create', GenericAPIView.as_view()),
    path('<int:id>', DetailsAPIView.as_view())
]