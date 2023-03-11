from django.shortcuts import render, redirect
from .models import Field
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core import serializers   
from laboratories.models import Laboratory
from django.http import HttpResponseRedirect

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
    fields = Field.objects.select_related('laboratory').filter(laboratory = lab_id)
    laboratory = Laboratory.objects.get(id = lab_id)

    context = {'entity': fields, 'lab': laboratory}

    return render(request, 'lab_fields.html', context)

@login_required
def remove(request, id):
    Field.objects.get(id = id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def edit_field(request, id):
    field = Field.objects.get(id = id)
    laboratories = Laboratory.objects.all()
    context = {'field': field, 'laboratories': laboratories}

    return render(request, 'edit_field.html', context)