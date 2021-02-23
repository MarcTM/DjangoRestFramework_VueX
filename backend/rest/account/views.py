from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Account
from meals.models import Meal
from .serializers import RegistrationSerializer, AccountProfileSerializer, AccountCartSerializer


# Register user
@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration successfull"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token

            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Validate token
@api_view(['GET'])
def validate_token(request):

    if request.method == 'GET':
        user = request.user
        if user:
            return Response("Valid token")



# Get user
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def account_profile(request):

    try:
        account = request.user
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountProfileSerializer(account)
        return Response(serializer.data)



# Update user
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_account_profile(request):

    try:
        account = request.user
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountProfileSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Profile update success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_cart(request, **kwargs):
    
    try:
        account = request.user    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountCartSerializer(account)
        return Response(serializer.data)



@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def account_cart(request, **kwargs):
    account = request.user

    try:
        meal = Meal.objects.get(id=kwargs.get('id'))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        account.add_to_cart(meal)
        return Response("OK")
    
    elif request.method == 'DELETE':
        account.remove_from_cart(meal)
        return Response("OK")