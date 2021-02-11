from .models import Category
from meals.models import Meal
from meals.serializers import MealSerializer
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    meals = MealSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['title', 'meals']
        # fields = '__all__'