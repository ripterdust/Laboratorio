from django.db import models

# Create your models here.
class Laboratory(models.Model):

    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(default=0.00, null=False)
