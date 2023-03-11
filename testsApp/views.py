from django.shortcuts import render, redirect
from .models import Test
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    tests = Test.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = { 'entity': tests, 'paginator': paginator }


    return render(request, 'tests.html', context)