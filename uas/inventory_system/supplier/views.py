from django.shortcuts import render, get_object_or_404, redirect
from store.models import StockOrder
from .models import Delivery
from .forms import DeliveryForm

def order_list(request):
    # Tampilkan pesanan yang belum terpenuhi atau sesuai kebutuhan
    orders = StockOrder.objects.filter(is_fulfilled=False)
    return render(request, 'supplier/order_list.html', {'orders': orders})

def delivery_update(request, order_id):
    order = get_object_or_404(StockOrder, id=order_id)
    # Pastikan setiap order hanya memiliki satu delivery, jika belum ada, buat baru
    delivery, created = Delivery.objects.get_or_create(stock_order=order)
    
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            # Jika pengiriman sudah delivered, tandai order sebagai terpenuhi
            if delivery.status == 'delivered':
                order.is_fulfilled = True
                order.save()
            return redirect('order_list')
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, 'supplier/delivery_form.html', {'form': form, 'order': order})
