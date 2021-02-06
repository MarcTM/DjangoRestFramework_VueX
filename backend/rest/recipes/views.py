from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets



# class RecipeViewSet(viewsets.ViewSet):

#     def list(self, request):
#         recipes = Recipe.objects.all()
#         serializer = RecipeSerializer(recipes, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = RecipeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Recipe.objects.all()
#         recipe = get_object_or_404(queryset, pk=pk)
#         serializer = RecipeSerializer(recipe)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         recipe = Recipe.objects.get(pk=pk)
#         serializer = RecipeSerializer(recipe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Get, create recipes
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)



# Get one, update, delete recipe
class DetailsAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = 'id'


    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)