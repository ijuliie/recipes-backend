from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ('id', 'created_at', 'owner', 'meal_of_the_day', 'ingredients', 'instructions', 'is_public')