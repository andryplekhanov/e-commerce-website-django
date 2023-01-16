from django.db import models
from django.utils.translation import gettext_lazy as _


class Vendor(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name=_('название'))
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name=_('url-адрес'))
    description = models.TextField(blank=True, verbose_name=_('описание'))
    address = models.TextField(blank=True, verbose_name=_('адрес'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('магазин')
        verbose_name_plural = _('магазины')

    def __str__(self):
        return self.name
