from . import views
from django.urls import path
app_name = 'about'
urlpatterns = [path('', views.about, name='about'),
path('contacs/', views.contacts, name='contacts'),
path('deliver/', views.deliver, name='deliver',)
               ]
