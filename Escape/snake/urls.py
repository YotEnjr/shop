from . import views
from django.urls import path

app_name = 'snake'
urlpatterns = [path('', views.index, name='start'),
               
               ]
