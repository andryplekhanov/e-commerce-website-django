from django.urls import path
from . import views
from .views import *

urlpatterns = [path('cart_detail/', CartDetail.as_view(), name='cart_detail'),
               path('add/<int:pk>/', views.cart_add, name='cart_add'),
               path('remove/<int:pk>/', views.cart_remove, name='cart_remove'),
               path('get_cart_data/', get_cart_data, name='get_cart_data'),
               ]
