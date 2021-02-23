from rest_framework import serializers
from .models import Account
from meals.serializers import MealSerializer


class RegistrationSerializer(serializers.ModelSerializer):

    rpassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'rpassword']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        rpassword = self.validated_data['rpassword']

        if password != rpassword:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password(password)
        
        account.save()
        return account


class AccountProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'email', 'username']


class AccountCartSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'email', 'meals']