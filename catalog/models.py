from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    img = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=60, verbose_name='категория', **NULLABLE)
    price_for_buy = models.IntegerField(verbose_name='цена за покупку', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания', **NULLABLE)
    last_change_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    class META:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    class META:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
