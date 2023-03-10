from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=255)
    measurment = models.CharField(max_length=255)