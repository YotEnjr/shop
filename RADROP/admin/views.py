#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def adminpage(request):
    return HttpResponse('Страница админа')