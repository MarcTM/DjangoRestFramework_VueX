from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from account.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from .models import Account


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


@api_view(['GET'])
def validate_token(request):

    if request.method == 'GET':
        user = request.user
        if user:
            return Response("Valid token")