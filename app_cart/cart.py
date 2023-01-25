from decimal import Decimal

from django.conf import settings
from django.shortcuts import redirect

from app_product.models import Product


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

    def __len__(self):
        """ Подсчет всех товаров в корзине. """
        return sum(item['quantity'] for item in self.cart.values())

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
                        value['quantity'] += 1
                        newItem = False
                        self.save()
                        break
            if newItem == True:
                self.cart[product.id] = {
                    'userid': self.request.user.id,
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

                value['quantity'] -= 1
                if (value['quantity'] < 1):
                    return redirect('cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        """ Опустошение корзины """

        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        """ Подсчет итоговой суммы """

        total_price = sum(float(item['price']) * item['quantity'] for item in self.cart.values())
        return Decimal.from_float(total_price).quantize(Decimal("1.00"))

    def get_all_ids(self):
        """ Получить список id продуктов в корзине  """

        return [item.get('product_id') for item in self.cart.values()]

    def __iter__(self):
        """ Перебор элементов в корзине и получение продуктов из базы данных. """

        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = Decimal.from_float(item['price'] * item['quantity']).quantize(Decimal("1.00"))
            yield item
