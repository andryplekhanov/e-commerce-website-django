# from django.contrib.auth import get_user, get_user_model
# from django.db import models
# from app_product.models import Product
# from django.utils.translation import gettext_lazy as _
#
# User = get_user_model()
#
#
# class Cart_db(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('пользователь'), related_name='cart')
#     good = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('товар'), related_name='cart')
#     quantity = models.PositiveIntegerField(verbose_name=_('количество'))
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('цена'))
#
#     def __str__(self):
#         return f'Cart {self.user}'
#
#     class Meta:
#         verbose_name = _('корзина')
#         verbose_name_plural = _('корзины')
