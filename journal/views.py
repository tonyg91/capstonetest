from django.shortcuts import render
from .models.journal import Journals
from .models.supply import Supply
from .models.theme import Theme
from rest_framework import viewsets
from rest_framework import permissions
from journal.serializers import JournalSerializer, SupplySerializer, ThemeSerializer

class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Journals.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.AllowAny]

class SupplyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [permissions.AllowAny]


class ThemeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [permissions.AllowAny]
