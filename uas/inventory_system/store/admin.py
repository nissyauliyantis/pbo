from django.contrib import admin
from .models import Product, StockOrder

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    search_fields = ['name']

@admin.register(StockOrder)
class StockOrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'order_date', 'is_fulfilled']
    list_filter = ['is_fulfilled', 'order_date']

