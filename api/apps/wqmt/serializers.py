from rest_framework import serializers
from .models import WQMT # , DeliveryInfo

class WQMTSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = WQMT
    fields = ('url', 'pk', 'delivery', 'issue_category', 'issue', 'detail', 'created_at', 'updated_at') #, 'score')

# class DeliverySerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = DeliveryInfo
#     fields = '__all__'