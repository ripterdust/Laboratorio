from django.shortcuts import render
from .models import Laboratory

# Create your views here.
def home(request):
    laboratories = Laboratory.objects.all()

    context = {'entity': laboratories}

    return render(request, 'laboratories.html', context)