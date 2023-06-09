
from .models import Test
from clientes.models import Clients
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import render, redirect
from fields.models import Field
from laboratories.models import Laboratory
from laboratorio.utils import render_to_pdf
from testResultFields.models import TestResultField

# Create your views here.


@login_required
def index(request):

    tests = Test.objects.order_by(
        '-created_at').select_related('patient', 'lab')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = {'entity': tests, 'paginator': paginator}

    return render(request, 'tests.html', context)


@login_required
def fill_fields(request, test_id):
    test = Test.objects.select_related('patient', 'lab').get(id=test_id)

    if test.completed:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    fields = Field.objects.filter(laboratory=test.lab.id)

    context = {'test': test, 'fields': fields}

    return render(request, 'fill_fields.html', context)


@login_required
def completed_tests(request):
    tests = Test.objects.filter(completed=True).order_by(
        '-created_at').select_related('patient', 'lab')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = {'entity': tests, 'paginator': paginator}

    return render(request, 'completed_tests.html', context)


@login_required
def uncompleted_tests(request):
    tests = Test.objects.filter(completed=False).order_by(
        '-created_at').select_related('patient', 'lab')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tests, 10)
        clients = paginator.page(page)
    except:
        return redirect('/tests')

    context = {'entity': tests, 'paginator': paginator}

    return render(request, 'state_tests.html', context)


@login_required
def save_uncompleted_test(request, test_id):
    post = request.POST

    test = Test.objects.get(id=test_id)

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
    test.comment = post.get('comment')
    test.save()

    messages.success(request, 'Test completado con éxito')

    return HttpResponseRedirect('/tests/completed')


def send_pdf(request, test_id):
    test = Test.objects.select_related('patient', 'lab').get(id=test_id)

    if not test.completed:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    fields = TestResultField.objects.filter(
        test=test_id).select_related('field')

    context = {
        'lab_name': 'Nombre laboratorio',
        'address': '52 avenida a 6-23 residenciales naciones unidas 2, zona 10 villa nueva',
        'phone': '35420928',
        'test': test,
        'fields': fields
    }

    pdf = render_to_pdf('result.html', context)

    return HttpResponse(pdf, content_type='application/pdf')


@login_required
def new_test(request):

    clients = Clients.objects.all().only('name', 'dpi', 'id')
    laboratories = Laboratory.objects.all().only('name', 'id', 'price')

    context = {
        'clients': clients,
        'laboratories': laboratories
    }

    return render(request, 'new_test.html', context)


@login_required
def store_new_test(request):
    post = request.POST.get

    patient = post('client')
    lab = post('lab')

    laboratory = Laboratory.objects.get(id=lab)
    client = Clients.objects.get(id=patient)
    test = Test()
    test.lab = laboratory
    test.patient = client

    test.save()

    messages.success(request, 'Se ha creado el test correctamente')
    return redirect('/tests/uncompleted/')


@login_required
def delete_test(request, test_id):
    test = Test.objects.get(id=test_id)

    if not test.completed:
        test.delete()

    messages.error(request, 'Se ha eliminado el test correctamente')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
