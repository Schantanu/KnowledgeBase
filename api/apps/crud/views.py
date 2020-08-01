from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import CRUD
from .serializers import CRUDSerializer


class CRUDViewSet(viewsets.ModelViewSet):
    queryset = CRUD.objects.all()
    serializer_class = CRUDSerializer

    # http_method_names = ['get','post','head']
    filter_backends = (filters.SearchFilter, )
    search_fields = ('delivery', 'issue_category', 'issue', 'detail',
                     'created_at', 'updated_at')
