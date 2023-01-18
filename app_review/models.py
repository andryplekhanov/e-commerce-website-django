from django.contrib.auth import get_user_model
from django.db import models
from app_product.models import Product
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('пользователь'), related_name='review')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('товар'), related_name='review')
    text = models.TextField(verbose_name=_('отзыв'), max_length=1000)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))

    def __str__(self):
        return f'Review for {self.product.name}'

    class Meta:
        verbose_name = _('отзыв')
        verbose_name_plural = _('отзывы')
