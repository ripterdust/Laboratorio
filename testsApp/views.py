from django.shortcuts import render, redirect
from .models import Test
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def index(request):

    tests = Test.objects.select_related('patient', 'lab')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = { 'entity': tests, 'paginator': paginator }


    return render(request, 'tests.html', context)

@login_required
def fill_fields(request, test_id):
    test =  tests = Test.objects.select_related('patient', 'lab').get(id = test_id)

    context = {'test': test}


    return render(request, 'fill_fields.html', context)

@login_required
def completed_tests(request):
    tests = Test.objects.filter(completed=True).select_related('patient', 'lab')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = { 'entity': tests, 'paginator': paginator }


    return render(request, 'completed_tests.html', context)

@login_required
def uncompleted_tests(request):
    tests = Test.objects.filter(completed=False).select_related('patient', 'lab')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = { 'entity': tests, 'paginator': paginator }


    return render(request, 'state_tests.html', context)
