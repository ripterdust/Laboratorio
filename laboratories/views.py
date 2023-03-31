from django.shortcuts import render, redirect
from .models import Laboratory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from fields.models import Field
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


@login_required
def home(request):
    laboratories = Laboratory.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(laboratories, 10)
        laboratories = paginator.page(page)
    except:
        return redirect('/laboratories')

    context = {'entity': laboratories, 'paginator': paginator}

    return render(request, 'laboratories.html', context)


@login_required
def delete(request, id):
    try:
        Laboratory.objects.get(id=id).delete()
        messages.success(request, 'Laboratorio eliminado correctamente!')
        return redirect('/laboratories')
    except:
        messages.error(request, 'No se pudo eliminar el laboratorio')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def edit(request, id):
    laboratory = Laboratory.objects.get(id=id)
    related_fields = Field.objects.filter(laboratory=id)
    context = {'lab': laboratory, 'related_fields': related_fields,
               'related_count': related_fields.count()}

    return render(request, 'edit_lab.html', context)


@login_required
def store(request, id):
    try:

        form = request.POST

        laboratory = Laboratory.objects.get(id=id)
        laboratory.name = form.get('name')
        laboratory.price = form.get('price')
        laboratory.save()

        messages.success(request, 'Laboratorio editado correctamente!')

    except:
        messages.error(request, 'Error al editar el laboratorio')

    return redirect('/laboratories/')


@login_required
def new_lab(request):
    return render(request, 'new_lab.html')


def store_lab(request):
    post = request.POST

    laboratory = Laboratory()

    laboratory.name = post.get('name')
    laboratory.price = post.get('price')

    laboratory.save()

    lab_id = laboratory.id

    messages.success(request, 'Laboratorio creado correctamente!')

    return redirect(f'/laboratories/edit/{lab_id}')
