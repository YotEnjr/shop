# from django.shortcuts import render

# homepage/views.py
from django.http import HttpResponse

# Главная страница.


def index(request):
    return HttpResponse('Главная страница')

# def index(request):
#    return render(request, 'homepage/index.html', {})
