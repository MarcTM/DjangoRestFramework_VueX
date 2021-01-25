from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins


# Get, create recipes
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)



# Get one, update, delete recipe
class DetailsAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = 'id'


    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)