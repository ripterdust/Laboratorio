from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from clientes.models import Clients
from laboratories.models import Laboratory
from testsApp.models import Test
from datetime import datetime, timedelta, date
from django.db.models import Sum
from calendar import monthrange

# Create your views here.
@login_required
def dashboard(request):

    last_month = datetime.today() - timedelta(days=30)
    clients = Clients.objects.all().count()
    laboratories = Laboratory.objects.all().count()
    tests = Test.objects.filter(created_at__gte=last_month)
    test_count = tests.count()
    total_sales = tests.select_related('lab').aggregate(sum=Sum('lab__price'))['sum']

    sales_by_month = []
    today = date.today()
    year = today.year
    month = today.month

    for i in range(1, monthrange(year, month)[1] + 1):
        test_month = Test.objects.filter(
            created_at__gte=last_month, 
            created_at__year__gte = year, 
            created_at__day__gte = i, 
            created_at__day__lte =i
        )
        sales = test_month.select_related('lab').aggregate(sum=Sum('lab__price'))['sum']

        if not sales:
            sales = 0

        sales_by_month.append(sales)

    context = {'total_clients': clients, 
        'total_laboratories': laboratories, 
        'total_tests': test_count, 
        'total_sales': total_sales,
        'data': sales_by_month
    }

    return render(request, 'home.html', context)