from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        # fields = ['id', 'title', 'description']
        fields = '__all__'