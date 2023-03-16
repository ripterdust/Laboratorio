from django.db import models
import datetime
# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=255, default='N/A', null=False)
    birth = models.DateField(default=datetime.date.today, auto_now=False)
    dpi = models.CharField(max_length=20, null=False, default='N/A')
    email = models.EmailField(default='n/a', null=False)
    sex = models.IntegerField(default=1)
    nit = models.CharField(max_length=20, default='N/A')
    created_at = models.DateField(auto_now=True)

    def __str__(self)->str:
        return f'{self.name}-{self.dpi}'