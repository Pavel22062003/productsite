# Generated by Django 4.2.1 on 2023-05-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_blog_view_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='URL'),
        ),
    ]
