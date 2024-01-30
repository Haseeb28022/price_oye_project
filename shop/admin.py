from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'stock_quantity', 'brand', 'category')
    list_filter = ('brand', 'category')
    search_fields = ('name', 'brand__name', 'category__name')


admin.site.register(Product, ProductAdmin)
