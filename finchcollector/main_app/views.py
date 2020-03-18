from django.shortcuts import render
from .models import Finch

# Add the Cat class & list and view function below the imports


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello Finches</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches' : finches})