from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def destination(request, id=1):
    data = Destinations.objects.get(pk=id)
    return render(request, 'destination.html', {'data': data})


def crew(request, id=1):
    data = Crew.objects.get(pk=id)
    return render(request, 'crew.html', {'data': data})


def technology(request, id):
    data = Technology.objects.get(pk=id)
    return render(request, 'technology.html', {'data': data})
