from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('delivery/<int:order_id>/', views.delivery_update, name='delivery_update'),
]
