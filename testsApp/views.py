from django.shortcuts import render, redirect
from .models import Test
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from fields.models import Field
from testResultFields.models import TestResultField

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
    test = Test.objects.select_related('patient', 'lab').get(id = test_id)

    if test.completed:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
    fields = Field.objects.filter(laboratory=test.lab.id)

    context = {'test': test, 'fields': fields}


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


@login_required
def save_uncompleted_test(request, test_id):
    post = request.POST

    test = Test.objects.get(id = test_id)

    if test.completed:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    fields_string = post.get('fields')

    fields_dict = eval(fields_string)
    fields_list = list(fields_dict.keys())

    for field in fields_list:
        data_field = Field.objects.get(id=int(field))
        test_result_field = TestResultField()
        
        actual_field = fields_dict[field]
        test_result_field.field = data_field
        test_result_field.result = actual_field
        test_result_field.test = test

        test_result_field.save()

    
    test.completed = True
    test.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))