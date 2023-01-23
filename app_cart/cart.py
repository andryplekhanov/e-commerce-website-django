from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


class Cart(object):

    def __init__(self, request):
        """ Инициализируем корзину """

        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем пустую корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """ Добавляем товар в корзину или обновляем его количество. """

        id = product.id
        newItem = True

        image = product.images.first()
        if image:
            image = str(image.image.url)

        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.name,
                'quantity': 1,
                'price': str(product.price),
                'description': product.get_clear_description(),
                'url': product.get_absolute_url(),
                'image': image,
                'stock': product.stock
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    if value['quantity'] >= product.stock:
                        newItem = False
                        self.save()
                        break
                    else:
                        value['quantity'] = value['quantity'] + 1
                        newItem = False
                        self.save()
                        break
            if newItem == True:
                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    'description': product.get_clear_description(),
                    'url': product.get_absolute_url(),
                    'image': image,
                    'stock': product.stock
                }
        self.save()

    def save(self):
        """ Обновление корзины в сессии """

        self.session[settings.CART_SESSION_ID] = self.cart
        # помечаем сессию как изменённую, чтобы убедиться в сохранении
        self.session.modified = True

    def remove(self, product):
        """ Удаление продукта из корзины """

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        """ Уменьшение количества товара на 1 ед. """

        for key, value in self.cart.items():
            if key == str(product.id):

                value['quantity'] = value['quantity'] - 1
                if (value['quantity'] < 1):
                    return redirect('cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        """ Пустая корзина """

        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        """ Подсчет итоговой суммы """

        total_price = sum(float(item['price']) * item['quantity'] for item in self.cart.values())
        return Decimal.from_float(total_price).quantize(Decimal("1.00"))
