"""django_restframework serializers for the app models"""
from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    """Full rest api serializer for the data model."""

    class Meta:
        model = Data
        fields = ('id', 'name')
