"""'Standard django models."""
from django.db import models

# Create your models here.
class Data(models.Model):
    """Example data for the demo app"""

    name = models.CharField(max_length=100)
