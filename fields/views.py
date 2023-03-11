from django.shortcuts import render, redirect
from .models import Field
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core import serializers   

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