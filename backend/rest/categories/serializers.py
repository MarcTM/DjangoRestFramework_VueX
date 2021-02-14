from .models import Category
from meals.models import Meal
from meals.serializers import MealSerializer
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class CategoryMealsSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'meals']