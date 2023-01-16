from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]