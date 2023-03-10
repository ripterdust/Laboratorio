from django.shortcuts import render, redirect
from .models import Laboratory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

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