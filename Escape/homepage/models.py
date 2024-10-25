from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.SlugField(unique=True)


class Products(models.Model):
    title = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    size = models.IntegerField()
    price = models.IntegerField()


