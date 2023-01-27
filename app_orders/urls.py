from django.urls import path
from app_orders.views import *

urlpatterns = [
    path('all/', OrdersHistory.as_view(), name='orders_history'),
    path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('create/', OrderView.as_view(), name='order_create'),

]
