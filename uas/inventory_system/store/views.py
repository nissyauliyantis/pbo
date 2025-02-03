from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, StockOrder
from .forms import ProductForm, StockOrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

def stock_report(request):
    # Contoh sederhana: filter produk dengan stok dibawah threshold (misalnya 5)
    low_stock_products = Product.objects.filter(stock__lte=5)
    return render(request, 'store/stock_report.html', {'products': low_stock_products})

def order_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = StockOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('product_list')
    else:
        form = StockOrderForm()
    return render(request, 'store/order_form.html', {'form': form, 'product': product})

