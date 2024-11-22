from django.shortcuts import render, get_object_or_404
from homepage.models import Categories, Products
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm


def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    category_list = Categories.objects.all()
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'category_list': category_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)


@login_required
def catalog(request):
    template_name = 'homepage/catalog.html'
    # Возьмём нужное. А ненужное не возьмём:
    product_list = Products.objects.values('id', 'title', 'price')
    context = {
        'product_list': product_list,
    }
    return render(request, template_name, context)


def product_detail(request, id, slug):
    product = get_object_or_404(Products,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


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
