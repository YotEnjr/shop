#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def catalog(request):
    return HttpResponse('каталог товаров')