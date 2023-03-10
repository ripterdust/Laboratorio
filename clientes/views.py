from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Clients

# Create your views here.
@login_required
def clients(request):

    clients = Clients.objects.all()

    context = { 'clients': clients }

    return render(request, 'clientes.html', context)

def client_by_id(request, id):
    return redirect('/clients')