from . import views
from django.urls import path

app_name = 'homepage'
urlpatterns = [path('', views.index, name='index'),
path('catalog/', views.catalog, name='catalog'),
               ]
"""
path('catalog/<slug>/', views.category, name='category'),
path('catalog/<pk>/', views.vesch, name='vecsh')
"""