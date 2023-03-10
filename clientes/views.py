from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Clients
from django.core.paginator import Paginator

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