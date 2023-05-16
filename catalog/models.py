from django.db import models
from django.urls import reverse

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


class Blog(models.Model):

    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания')
    publication_sign = models.BooleanField(verbose_name='признак публикации', default=True)
    view_amount = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.header



    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
