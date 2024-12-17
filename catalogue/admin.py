from django.contrib import admin

from .models import Category, Product, ProductClass

admin.site.register(Product)
admin.site.register(ProductClass)
admin.site.register(Category)
