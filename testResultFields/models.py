from django.db import models
from testsApp.models import Test
# Create your models here.
class TestResultField(models.Model):
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, null=False)
    result = models.CharField(max_length=255, null=False)
    measurment = models.CharField(max_length=255, null=False)