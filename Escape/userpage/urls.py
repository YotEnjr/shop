#from django.contrib import admin
#from django.urls import path, include
from . import views
from django.urls import path
app_name = 'user'
urlpatterns = [path('', views.userpage, name='userpage'),
path('basket/', views.basket, name='basket')
               ]