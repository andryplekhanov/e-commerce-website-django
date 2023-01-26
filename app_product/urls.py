from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('catalog/', CategoryView.as_view(), name='catalog'),
    path('catalog/<str:slug>/', CategoryView.as_view(), name='catalog_for_category'),
]
