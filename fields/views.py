from .models import Field
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from laboratories.models import Laboratory

# Create your views here.


@login_required
def index(request):
    field = Field.objects.all().select_related('laboratory')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(field, 10)
        field = paginator.page(page)
    except:
        return redirect('/fields')

    context = {'entity': field, 'paginator': paginator}

    return render(request, 'fields.html', context)


@login_required
def fields_by_lab_id(request, lab_id):
    fields = Field.objects.select_related(
        'laboratory').filter(laboratory=lab_id)
    laboratory = Laboratory.objects.get(id=lab_id)

    context = {'entity': fields, 'lab': laboratory}

    return render(request, 'lab_fields.html', context)


@login_required
def remove(request, id):
    Field.objects.get(id=id).delete()
    messages.error(request, 'Campo eliminado correctamente!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def edit_field(request, id):
    field = Field.objects.get(id=id)
    laboratories = Laboratory.objects.all()
    context = {'field': field, 'laboratories': laboratories}

    return render(request, 'edit_field.html', context)


@login_required
def store(request, id):
    get = request.POST

    field = Field.objects.get(id=id)
    laboratory = Laboratory.objects.get(id=int(get.get('laboratory')))

    field.laboratory = laboratory
    field.name = get.get('name')
    field.measurment = get.get('measurment')
    field.reference = get.get('reference')
    field.save()

    messages.success(request, 'Campo editado correctamente!')
    return redirect('/fields')


@login_required
def store_by_edit_lab(request, lab_id):
    post = request.POST

    lab = Laboratory.objects.get(id=lab_id)

    field = Field()
    field.name = post.get('name')
    field.measurment = post.get('measurment')
    field.laboratory = lab
    field.reference = post.get('reference')
    field.save()

    messages.success(request, 'Campo creado correctamente!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
