from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from clientes.models import Clients
from laboratories.models import Laboratory
from testsApp.models import Test
from datetime import datetime, timedelta
from django.db.models import Sum

# Create your views here.
@login_required
def dashboard(request):

    last_month = datetime.today() - timedelta(days=30)
    clients = Clients.objects.all().count()
    laboratories = Laboratory.objects.all().count()
    tests = Test.objects.filter(created_at__gte=last_month)
    test_count = tests.count()
    total_sales = tests.select_related('lab').aggregate(sum=Sum('lab__price'))['sum']

    context = {'total_clients': clients, 'total_laboratories': laboratories, 'total_tests': test_count, 'total_sales': total_sales}

    return render(request, 'home.html', context)