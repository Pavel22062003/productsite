from django.db import models
from django.urls import reverse

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'категория - {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    img = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)

    price_for_buy = models.IntegerField(verbose_name='цена за покупку', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания', **NULLABLE)
    last_change_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    author = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE, **NULLABLE)
    publication_sign = models.BooleanField(verbose_name='признак публикации', default=False, **NULLABLE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'can_ban_publication_product',
                'can ban publication'
            ),
            (
                'can_change_description_product',
                'can change decription'
            ),
            (
                'can_change_category_product',
                'can change category'
            )
        ]

    def __str__(self):
        return f'{self.name}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    version_sign = models.BooleanField(verbose_name='признак версии', default=False)

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания', auto_now=True)
    publication_sign = models.BooleanField(verbose_name='признак публикации', default=False)
    view_amount = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

