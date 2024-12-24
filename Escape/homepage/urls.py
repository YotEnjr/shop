from . import views
from django.urls import path

app_name = 'homepage'
urlpatterns = [path('', views.index, name='index'),
               path('main/', views.main, name='main'),
               path('snake/', views.snake, name='snake'),
               path('product_detail/<id>', views.product_detail,
                    name='product_detail')
               ]
"""
path('catalog/<slug>/', views.category, name='category'),
path('catalog/<pk>/', views.vesch, name='vecsh')
"""
