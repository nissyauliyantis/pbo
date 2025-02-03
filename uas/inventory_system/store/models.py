from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)  # memastikan tidak ada duplikasi
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.name

class StockOrder(models.Model):
    """
    Model untuk mencatat pesanan restock produk.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"
