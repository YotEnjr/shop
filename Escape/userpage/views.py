from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
# Create your views here.


@login_required
def userpage(request):
    return render(request, 'userpage/userpage.html', {})


@login_required
def basket(request):
    return render(request, 'userpage/basket.html', {})