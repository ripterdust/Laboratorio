from .models import Clients
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from testsApp.models import Test
import datetime

# Create your views here.


@login_required
def clients(request):
    clients = []

    search = ''

    if request.method == 'POST':
        search = request.POST.get('search')

        clients = Clients.objects.filter(name__contains=search)

    else:
        clients = Clients.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(clients, 10)
        clients = paginator.page(page)
    except:
        return redirect('/clients')

    context = {'entity': clients, 'paginator': paginator, 'search': search}

    return render(request, 'clientes.html', context)


@login_required
def client_by_id(request, id):
    return redirect('/clients')


@login_required
def delete(request, id):
    try:
        Clients.objects.get(id=id).delete()
        messages.success(request, 'Cliente eliminado correctamente!')
        return redirect('/clients')
    except:
        messages.error(request, 'No se pudo eliminar el cliente')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def edit(request, id):
    client = Clients.objects.get(id=id)
    tests = Test.objects.filter(patient=id).count()

    context = {'client': client, 'tests': tests}

    return render(request, 'edit.html', context)


@login_required
def store(request, id):
    form = request.POST

    client = Clients.objects.get(id=id)
    client.name = form.get('name')
    client.dpi = form.get('dpi')
    client.birth = form.get('birth')
    client.email = form.get('email')
    client.sex = form.get('sex')
    client.nit = form.get('nit')
    client.phone = form.get('phone')
    client.save()

    messages.success(request, 'Cliente editado correctamente!')
    return redirect('/clients/')


@login_required
def history(request, id):
    client = Clients.objects.get(id=id)
    tests = Test.objects.filter(patient=id).select_related('lab')

    context = {
        'client': client,
        'tests': tests
    }

    return render(request, 'history.html', context)


def new_client(request):

    return render(request, 'new_client.html')


def save_new_patient(request):
    post = request.POST.get

    client = Clients()
    client.name = post('name')
    client.email = post('email')
    client.dpi = post('dpi')
    client.birth = post('birth')
    client.sex = post('sex')
    client.nit = post('nit')
    client.phone = post('phone')
    client.save()

    messages.success(request, 'Cliente creado correctamente!')
    return redirect('/clients')
