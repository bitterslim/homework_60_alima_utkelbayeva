from django.contrib import admin

from webapp.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category',  'image', 'leftover', 'price']
