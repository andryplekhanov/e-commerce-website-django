from app_cart.cart import Cart


def cart(request):
    cart = Cart(request)
    total_bill = 0.0
    total_items = 0
    for key, value in request.session['cart'].items():
        total_bill += (float(value['price']) * value['quantity'])
        total_items += value['quantity']
    return {'cart_total_price': total_bill, 'cart_total_items': total_items}
