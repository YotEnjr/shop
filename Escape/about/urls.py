from . import views
from django.urls import path
app_name = 'about'
urlpatterns = [path('', views.about, name='about'),
               path('contact/', views.contact, name='contact'),
               path('deliver/', views.deliver, name='deliver'),
               path('payment/', views.payment, name='payment'),
               ]
