from django.contrib.auth.models import AbstractUser
from django.db import models

# from catalog.models import NULLABLE
NULLABLE = {'blank': True, 'null': True}

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',**NULLABLE)
    country = models.CharField(verbose_name='страна',**NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

