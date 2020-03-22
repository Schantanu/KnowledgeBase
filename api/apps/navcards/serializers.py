from rest_framework import serializers
# from .models import Recipe
from .models import NavCards

# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = ("id", "name", "ingredients", "picture", "difficulty",
#                   "prep_time", "prep_guide")


class NavCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavCards
        fields = ("id", "project", "page", "title", "source", "description")