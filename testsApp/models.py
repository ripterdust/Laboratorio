from django.db import models
from clientes.models import Clients
from laboratories.models import Laboratory
import datetime
# Create your models here.
class Test(models.Model):
    patient = models.ForeignKey(Clients, on_delete=models.PROTECT)
    lab = models.ForeignKey(Laboratory, on_delete=models.PROTECT)
    completed = models.BooleanField(default=False)
    comment = models.CharField(default='No hay comentarios', max_length=255)
    created_at = models.DateField(default=datetime.date.today)