from django.shortcuts import render, get_object_or_404
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets



# Get, create cateogries
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)



# Get category
class DetailsAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


    def get(self, request, id):
        return self.retrieve(request)