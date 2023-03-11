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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))