from django.db import models
from laboratories.models import Laboratory
# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=255)
    measurment = models.CharField(max_length=255)
    reference = models.CharField(max_length=255, default="No hay referencia")
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)


    def __str__(self)->str:
        return self.name