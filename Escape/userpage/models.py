from django.db import models
from homepage.models import Products
# Create your models here.


class Userpage(models.Model):
    login = models.CharField(
        max_length=128, unique=True, verbose_name='типо логин')
    password = models.CharField(
        max_length=32, verbose_name='пароль(надо шифрование придкмать)')
    email = models.CharField(max_length=128, unique=True,
                             verbose_name='почта бедолаги(тоже шифр нужен)')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login


class UserBasket(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,
                                related_name='UserToBasket', verbose_name='Продукт из каталога')
    count = models.IntegerField(verbose_name='Кол-во шт.')

    class Meta:
        verbose_name = 'Карзина(заказ) Пользователя'
        verbose_name_plural = 'Карзины(заказы) Пользователя'
