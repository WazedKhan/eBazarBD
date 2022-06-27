from django.contrib import admin

from product.models import Category, SubCategory, Brand, Product

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
