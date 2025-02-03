from django import forms
from .models import Product, StockOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']

class StockOrderForm(forms.ModelForm):
    class Meta:
        model = StockOrder
        fields = ['quantity']
