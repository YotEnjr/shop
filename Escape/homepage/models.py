from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.SlugField(unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title 

class Products(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='Название')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    size = models.IntegerField(verbose_name='Размер')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Вещь(1шт)'
        verbose_name_plural = 'Товары(много)'
    def __str__(self):
        return self.title 
