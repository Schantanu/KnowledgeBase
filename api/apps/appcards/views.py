from django.shortcuts import render

from rest_framework import viewsets
from .serializers import AppCardsSerializer
from .models import AppCards


class AppCardsViewSet(viewsets.ModelViewSet):
    serializer_class = AppCardsSerializer
    queryset = AppCards.objects.all()
    # http_method_names = ['get','post','head']
