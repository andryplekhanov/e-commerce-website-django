from django.urls import path
from app_cart.views import *

urlpatterns = [
    path('add/<int:pk>/', cart_add, name='cart_add'),
    path('item_clear/<int:pk>/', item_clear, name='item_clear'),
    path('item_increment/<int:pk>/', item_increment, name='item_increment'),
    path('item_decrement/<int:pk>/', item_decrement, name='item_decrement'),
    path('cart_clear/', cart_clear, name='cart_clear'),
    path('cart-detail/', cart_detail, name='cart_detail'),
]
