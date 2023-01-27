from django.db import models
from django.utils.translation import gettext_lazy as _
from .singleton_model import SingletonModel


class SiteSettings(SingletonModel):
    express_delivery_price = models.DecimalField(max_digits=10, decimal_places=2,
                                                 verbose_name=_('цена экспресс доставки'))
    edge_for_free_delivery = models.DecimalField(max_digits=10, decimal_places=2,
                                                 verbose_name=_('порог бесплатной доставки'))
    common_delivery_price = models.DecimalField(max_digits=10, decimal_places=2,
                                                verbose_name=_('цена обычной доставки'))
    root_category = models.ForeignKey('app_product.Category', on_delete=models.CASCADE,
                                      verbose_name=_('корневая категория каталога'), related_name='root_category',
                                      blank=True, null=True)
    category_main_page = models.ManyToManyField('app_product.Category',
                                                verbose_name=_('категории для показа на главной странице (максимум 3)'))
    quantity_popular = models.PositiveIntegerField(verbose_name=_('количество популярных товаров на главной странице'),
                                                   default=8)
    time_cache_product = models.PositiveIntegerField(verbose_name=_('через сколько дней кэшировать данные о продукте'),
                                                     default=1)

    def __str__(self):
        return str(_('настройки'))

    class Meta:
        verbose_name = _('настройки')
        verbose_name_plural = _('настройки')
