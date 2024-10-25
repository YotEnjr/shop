from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def userpage(request):
    return render(request, 'userpage/userpage.html', {})
    
def basket(request):
    return render(request, 'userpage/basket.html', {})