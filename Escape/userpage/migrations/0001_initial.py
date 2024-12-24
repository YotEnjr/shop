# Generated by Django 3.2.16 on 2024-12-24 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=128, unique=True, verbose_name='типо логин')),
                ('password', models.CharField(max_length=32, verbose_name='пароль(надо шифрование придкмать)')),
                ('email', models.CharField(max_length=128, unique=True, verbose_name='почта бедолаги(тоже шифр нужен)')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Кол-во шт.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserToBasket', to='homepage.products', verbose_name='Продукт из каталога')),
            ],
            options={
                'verbose_name': 'Карзина(заказ) Пользователя',
                'verbose_name_plural': 'Карзины(заказы) Пользователя',
            },
        ),
    ]
