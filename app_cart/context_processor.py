from app_cart.cart import Cart
from decimal import Decimal


def cart(request):
    cart = Cart(request)
    total_bill = 0.0
    total_items = 0
    for key, value in request.session['cart'].items():
        total_bill += (float(value['price']) * value['quantity'])
        total_items += value['quantity']
    return {'cart_total_price': Decimal.from_float(total_bill).quantize(Decimal("1.00")),
            'cart_total_items': total_items}
