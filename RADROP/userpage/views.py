#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def userpage(request):
    return HttpResponse('Личная страница пользователя')