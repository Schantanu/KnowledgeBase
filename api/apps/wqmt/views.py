from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import WQMT
from .serializers import WQMTSerializer

class WQMTViewSet(viewsets.ModelViewSet):
    queryset = WQMT.objects.all()
    serializer_class =  WQMTSerializer

    # http_method_names = ['get','post','head']
    filter_backends = (filters.SearchFilter,)
    search_fields = ('delivery', 'issue_category', 'issue', 'detail', 'created_at', 'updated_at')
