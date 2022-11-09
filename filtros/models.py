from django.db import models
from bens.models import Product
from model_utils.models import TimeStampedModel

# Create your models here.

class Filtros(TimeStampedModel):
    porsetor = models.ForeignKey(
        Product, related_name="porsetor", on_delete=models.CASCADE 
    )
    
