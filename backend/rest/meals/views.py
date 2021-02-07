from django.shortcuts import render, get_object_or_404
from .models import Meal
from .serializers import MealSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets



# class MealViewSet(viewsets.ViewSet):

#     def list(self, request):
#         meals = Meal.objects.all()
#         serializer = MealSerializer(meals, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = MealSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Meal.objects.all()
#         meal = get_object_or_404(queryset, pk=pk)
#         serializer = MealSerializer(meal)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         meal = Meal.objects.get(pk=pk)
#         serializer = MealSerializer(meal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Get, create meals
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = MealSerializer
    queryset = Meal.objects.all()
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



# Get one, update, delete meal
class DetailsAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    lookup_field = 'id'


    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)