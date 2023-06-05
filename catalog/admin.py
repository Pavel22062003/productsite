from django.contrib import admin

from catalog.models import Product, Category, Blog, Version

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number',)
