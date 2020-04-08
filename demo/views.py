"""The standard django views"""
from rest_framework import generics

from .models import Data
from .serializers import DataSerializer

class DataListCreate(generics.ListCreateAPIView):
    """Rest API for the Data model"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer
