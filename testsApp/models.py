from django.db import models
from clientes.models import Clients
from laboratories.models import Laboratory

# Create your models here.
class Test(models.Model):
    patient = models.ForeignKey(Clients, on_delete=models.PROTECT)
    lab = models.ForeignKey(Laboratory, on_delete=models.PROTECT)