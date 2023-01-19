from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from app_product.models import Product
from app_users.models import User
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


class Order(models.Model):
    DELIVERY_CHOICES = (
        ("1", _("Обычная доставка")),
        ("2", _("Экспресс доставка")),
    )

    PAYMENT_CHOICES = (
        ("1", _("Онлайн картой")),
        ("2", _("Онлайн со случайного чужого счета")),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('пользователь'), related_name='orders')
    delivery_type = models.CharField(max_length=30, choices=DELIVERY_CHOICES, verbose_name=_('способ доставки'),
                                     default="1")
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('стоимость доставки'),
                                         default=0)
    payment_type = models.CharField(max_length=30, choices=PAYMENT_CHOICES, verbose_name=_('способ оплаты'),
                                    default="1")
    address = models.CharField(max_length=255, verbose_name=_('адрес получателя'))
    city = models.CharField(max_length=100, verbose_name=_('город'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('дата изменения'))
    paid = models.BooleanField(default=False, verbose_name=_('оплачен'))
    card_number = models.PositiveIntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)],
                                              verbose_name=_('номер карты'))
    status = models.CharField(max_length=150, verbose_name=_('статус платежа'), blank=True, null=True)
    payment_code = models.IntegerField(default=0, verbose_name=_('код оплаты'))

    class Meta:
        ordering = ('-created',)
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')

    def __str__(self):
        return f'order {self.id}'

    def get_total_cost(self):
        total_cost = float(sum(item.get_cost() for item in self.items.all()) + self.delivery_price)
        return Decimal.from_float(total_cost).quantize(Decimal("1.00"))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name=_('заказ'))
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE,
                                verbose_name=_('продукт'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('цена'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('количество'))

    class Meta:
        verbose_name = _('товар')
        verbose_name_plural = _('товары')

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        total_cost = float(self.price * self.quantity)
        return Decimal.from_float(total_cost).quantize(Decimal("1.00"))
