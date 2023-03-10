from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Clients
from django.core.paginator import Paginator
import datetime

# Create your views here.
@login_required
def clients(request):
    clients = Clients.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(clients, 10)
        clients = paginator.page(page)
    except:
        return redirect('/clients')

    context = { 'entity': clients, 'paginator': paginator }

    return render(request, 'clientes.html', context)

def client_by_id(request, id):
    return redirect('/clients')

def delete(request, id):
    Clients.objects.get(id = id).delete()
    return redirect('/clients')

def edit(request, id):
    client = Clients.objects.get(id = id)

    print(client.birth)
    context = {'client': client}

    return render(request, 'edit.html', context)

def store(request, id):
    form = request.POST

    client = Clients.objects.get(id = id)
    client.name = form.get('name')
    client.dpi = form.get('dpi')
    client.birth = form.get('birth')
    client.email = form.get('email')
    client.sex = form.get('sex')
    client.save()    
    return redirect('/clients/edit/45')

