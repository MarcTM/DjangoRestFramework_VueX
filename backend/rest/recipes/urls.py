from django.urls import path
from .views import GenericAPIView, DetailsAPIView

urlpatterns = [
    path('recipes/', GenericAPIView.as_view()),
    path('recipes/<int:id>', DetailsAPIView.as_view())
]