from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)