from rest_framework import serializers
from .models import AppCards 

class AppCardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppCards
        fields = ("id", "project", "page", "title", "source", "description")