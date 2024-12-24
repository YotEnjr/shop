from django.shortcuts import render, get_object_or_404
from homepage.models import Categories, Products
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm


def index(request):
    template_name = 'homepage/index.html'
    # Полученный из БД QuerySet передаём в словарь контекста:
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, {})



def main(request):
    template_name = 'homepage/main.html'
    # Возьмём нужное. А ненужное не возьмём:
    product_list = Products.objects.all().filter(is_published=True)
    context = {
        'product_list': product_list,
    }
    return render(request, template_name, context)

@login_required
def product_detail(request, id):
    product = get_object_or_404(Products,
                                id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'homepage/product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def snake(request):
    template_name = 'snake/snake.html'
    return render(request, template_name, {})


# Будет еще одна вьюв функция для вызова странички отдельного товара как по арктиклю
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
