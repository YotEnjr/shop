from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return render(request, 'about/about.html', {})

def contacts(request):
    return render(request, 'about/contacts.html', {})

def deliver(request):
    return render(request, 'about/deliver.html', {})