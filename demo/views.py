"""The standard django views"""
from django.views.generic.base import TemplateView
from rest_framework import generics

from .models import Data
from .serializers import DataSerializer

class IndexView(TemplateView):
    """The main index view for the app"""
    template_name = "demo/index.html"

class DataListCreate(generics.ListCreateAPIView):
    """Rest API for the Data model"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer
