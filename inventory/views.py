from django.shortcuts import render, redirect
from .models import *
from .forms import *

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

def add_laptop(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/displayLaptops")
    else:
        form = LaptopForm()
        return render(request,"add_new.html",{"form":form})

def add_desktop(request):
    if request.method == 'POST':
        form = DesktopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/displayDesktops")
    else:
        form = DesktopForm()
        return render(request,"add_new.html",{"form":form})


def add_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/displayMobile")
    else:
        form = MobileForm()
        return render(request,"add_new.html",{"form":form})


