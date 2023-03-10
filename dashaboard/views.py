from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from clientes.models import Clients
from laboratories.models import Laboratory
# Create your views here.
@login_required
def dashboard(request):
    clients = Clients.objects.all().count()
    laboratories = Laboratory.objects.all().count()


    context = {'total_clients': clients, 'total_laboratories': laboratories}

    return render(request, 'home.html', context)