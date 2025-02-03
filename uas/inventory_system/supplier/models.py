from django.db import models
from store.models import StockOrder  # pastikan impor model dari app store

class Delivery(models.Model):
    stock_order = models.OneToOneField(StockOrder, on_delete=models.CASCADE, related_name='delivery')
    delivery_date = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                   help_text="Diskon yang ditawarkan oleh pemasok")

    def __str__(self):
        return f"Delivery for Order {self.stock_order.id} - {self.status}"

