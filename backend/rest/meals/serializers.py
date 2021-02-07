from .models import Meal
from rest_framework import serializers

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        # fields = ['id', 'title', 'description']
        fields = '__all__'