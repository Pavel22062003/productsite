from django.contrib import admin

from catalog.models import Product, Category, Blog

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('header',)}

admin.site.register(Blog, BlogAdmin)