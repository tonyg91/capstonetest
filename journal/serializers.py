from django.db import models
from rest_framework import serializers
from .models import Journals, Supply, Theme

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journals 
        fields = ['brand', 'paperweight', 'sizes', 'pages']
        
class SupplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supply
        fields = ['brand', 'type', 'ink']
        
class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theme
        fields = ['image', 'pagelayout', 'creator']