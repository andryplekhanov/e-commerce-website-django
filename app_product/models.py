from django.db import models
from django.db.models import Min
from django.urls import reverse
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _

from app_vendor.models import Vendor


class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('название'))
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name=_('url-адрес'))
    icon = models.FileField(upload_to='category/', blank=True, verbose_name=_('иконка'), db_index=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name=_('родительская категория'))
    image = models.ImageField(blank=True, upload_to='category/', verbose_name=_('изображение'), db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        ordering = ('name',)
        verbose_name = _('категория')
        verbose_name_plural = _('категории')

    def get_absolute_url(self):
        return reverse('product-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='category', verbose_name=_('категория'), db_index=True)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE, verbose_name=_('магазин'), db_index=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('название'))
    slug = models.SlugField(max_length=200, db_index=True, verbose_name=_('url-адрес'))
    description = models.TextField(blank=True, verbose_name=_('описание'), db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('цена'), db_index=True)
    stock = models.PositiveIntegerField(verbose_name=_('остаток'), db_index=True)
    available = models.BooleanField(default=True, verbose_name=_('доступен'), db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'), db_index=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('дата обновления'), db_index=True)
    manufacturer = models.CharField(max_length=50, db_index=True, verbose_name=_('производитель'))
    limited = models.BooleanField(default=False, verbose_name=_('ограниченная серия'), db_index=True)

    class Meta:
        ordering = ('price',)
        index_together = (('id', 'slug'),)
        verbose_name = _('продукт')
        verbose_name_plural = _('продукты')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk, self.slug])

    def __str__(self):
        return self.name


class ParameterName(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('характеристика'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('имя характеристики')
        verbose_name_plural = _('имена характеристик')


class Parameter(models.Model):
    parameter = models.ForeignKey(ParameterName, on_delete=models.CASCADE, related_name='parameter',
                                  verbose_name=_('название'), db_index=True)
    products = models.ManyToManyField('Product', blank=True, db_index=True, verbose_name=_('продукты'))
    value = models.ForeignKey('ParameterValue', on_delete=models.CASCADE, verbose_name=_('значение'),
                              related_name='parameter', db_index=True)

    def __str__(self):
        return f'{self.parameter.name}: {self.value.value}'

    class Meta:
        verbose_name = _('характеристика')
        verbose_name_plural = _('характеристики')


class ParameterValue(models.Model):
    value = models.CharField(max_length=255, verbose_name=_('значение'), unique=True, db_index=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = _('значение характеристики')
        verbose_name_plural = _('значения характеристик')


class Image(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name=_('изображение'))
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images', verbose_name=_('продукт'))

    class Meta:
        verbose_name = _('изображение')
        verbose_name_plural = _('изображения')
