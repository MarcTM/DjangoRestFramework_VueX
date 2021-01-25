from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Get, create recipes

class RecipeAPIView(APIView):

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True) 
        return Response(serializer.data)


    def post(self, request):
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



# Get one, update, delete recipe

class RecipeDetails(APIView):

    def get_object(self, id):
        try:
            return Recipe.objects.get(id=id)

        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        recipe = self.get_object(id)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, id):
        recipe = self.get_object(id)

        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = self.get_object(id)

        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)