from django.shortcuts import render

# homepage/views.py
#from django.http import HttpResponse

# Главная страница.


#def index(request):
#   return HttpResponse('Главная страница')


def index(request):
    return render(request, 'homepage/index.html', {})

def catalog(request):
    return render(request, 'homepage/catalog.html', {})

#Будет еще одна вьюв функция для вызова странички отдельного товара как по арктиклю
"""
def vesch(request, pk):
    context={'id':pk}
    return render(request, 'homepage/???.html', context)
"""
"""
def category(request, slug):
    context={'category':slug}
    return render(request, 'homepage/category.html', context)
"""