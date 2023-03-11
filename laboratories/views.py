from django.shortcuts import render, redirect
from .models import Laboratory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from fields.models import Field

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
    Laboratory.objects.get(id = id).delete()
    return redirect('/laboratories')

@login_required
def edit(request, id):
    laboratory = Laboratory.objects.get(id = id)
    related_fields = Field.objects.filter(laboratory=id)
    context = {'lab': laboratory, 'related_fields': related_fields}

    return render(request, 'edit_lab.html', context)


@login_required
def store(request, id):
    form = request.POST

    laboratory = Laboratory.objects.get(id = id)
    laboratory.name = form.get('name')
    laboratory.price = form.get('price')
    laboratory.save()    

    return redirect('/laboratories/')
