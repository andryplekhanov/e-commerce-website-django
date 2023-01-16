from django.shortcuts import render
from django.views.generic import DetailView

from app_product.models import Product


class ProductDetail(DetailView):
    model = Product
