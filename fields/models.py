from django.db import models
from laboratories.models import Laboratory
# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=255)
    measurment = models.CharField(max_length=255)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)