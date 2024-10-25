from django.db import models
from homepage.models import Products
# Create your models here.

class Userpage(models.Model):
    login = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=128, unique=True)


class UserBasket(Products):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='UserToBasket')
    count = models.IntegerField()

