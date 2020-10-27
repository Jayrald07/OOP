from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')


def displayLaptops(request):
    items = Laptop.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'index.html',context)

def displayDesktop(request):
    items = Desktop.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'index.html',context)

def displayMobile(request):
    items = Mobile.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'index.html',context)

