from django.db import models
from testsApp.models import Test
from fields.models import Field
# Create your models here.
class TestResultField(models.Model):
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    field = models.ForeignKey(Field, on_delete=models.PROTECT)
    result = models.CharField(max_length=255)