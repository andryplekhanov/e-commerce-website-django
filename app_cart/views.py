from django.shortcuts import render, redirect
from app_product.models import Product
from django.contrib.auth.decorators import login_required
from app_cart.cart import Cart


def cart_add(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.add(product=product)
    return redirect("cart_detail")


def item_clear(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'app_cart/cart.html')
