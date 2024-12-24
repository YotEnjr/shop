from . import views
from django.urls import path


app_name = 'user'
urlpatterns = [
    path('', views.userpage, name='userpage'),
    path('basket/', views.basket, name='basket'),
    path('register/', views.RegisterUser.as_view(), name='register'),
               ]