from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from app_product.models import *
from django.utils.translation import gettext_lazy as _


class ParameterValueInline(admin.TabularInline):
    model = Parameter.products.through


class ImageInline(admin.TabularInline):
    fk_name = 'product'
    model = Image


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'stock', 'available', 'limited', 'manufacturer', 'vendor', 'created', 'updated']
    list_filter = ['category', 'available', 'created', 'updated', 'limited', 'vendor', 'manufacturer']
    list_editable = ['price', 'stock', 'available', 'limited']
    save_on_top = True
    inlines = [ImageInline, ParameterValueInline]

    fieldsets = (
        (_('Информация о товаре'), {
            'fields': ('name', 'category', 'vendor', 'manufacturer', 'price', 'stock', 'available', 'limited'),
            'description': _('Информация о товаре')
        }),
        (_('Описание товара'), {
            'fields': ('description',),
            'description': _('<b>Вы можете использовать html-теги:</b><br><br>'
                             '&lt;h2&gt;Заголовок 2го уровня&lt;/h2&gt;<br>'
                             '&lt;h3&gt;Заголовок 3го уровня&lt;/h3&gt;<br>'
                             '&lt;p&gt;Параграф текста&lt;/p&gt;<br>'
                             '&lt;b&gt;Жирный текст&lt;/b&gt;<br>'
                             '&lt;i&gt;Текст курсивом&lt;/i&gt;<br><br>'
                             'Маркированный список:<br>'
                             '&lt;ul&gt;<br>'
                             '&lt;li&gt;пункт 1&lt;/li&gt;<br>'
                             '&lt;li&gt;пункт 2&lt;/li&gt;<br>'
                             '&lt;li&gt;пункт 3&lt;/li&gt;<br>'
                             '&lt;/ul&gt;<br><br>'
                             '<b>Ссылки и скрипты использовать нельзя!</b>')
        }),
    )


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'value', ]
    list_filter = ['parameter']
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ParameterName)
admin.site.register(ParameterValue)
