from django.contrib import admin
from .models import Product, ProductClass, Category

admin.site.register(Product)
admin.site.register(ProductClass)
admin.site.register(Category) 