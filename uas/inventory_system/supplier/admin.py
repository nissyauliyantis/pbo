from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['stock_order', 'status', 'delivery_date', 'discount']
    list_filter = ['status', 'delivery_date']

