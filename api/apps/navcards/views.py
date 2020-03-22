# from rest_framework import viewsets
# from .serializers import RecipeSerializer
# from .models import Recipe

# class RecipeViewSet(viewsets.ModelViewSet):
#     serializer_class = RecipeSerializer
#     queryset = Recipe.objects.all()

# from django.shortcuts import render

from rest_framework import viewsets
from .serializers import NavCardsSerializer
from .models import NavCards


class NavCardsViewSet(viewsets.ModelViewSet):
    serializer_class = NavCardsSerializer
    queryset = NavCards.objects.all()
    # http_method_names = ['get', 'post', 'head']
