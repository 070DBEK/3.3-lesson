from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    ordering = ('name',)
    list_editable = ('price', 'stock')

