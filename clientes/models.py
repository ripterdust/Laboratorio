from django.db import models
import datetime
# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=255, default='N/A', null=False)
    birth = models.DateField(default=datetime.date.today)
    dpi = models.CharField(max_length=20, null=False, default='N/A')
    created_at = models.DateField(auto_now=True)