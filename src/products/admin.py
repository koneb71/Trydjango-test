from django.contrib import admin

from .models import Product, ProductCondition

admin.site.register(Product)
admin.site.register(ProductCondition)