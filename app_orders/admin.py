from django.contrib import admin
from app_orders.models import OrderItem, Order
from django.utils.translation import gettext_lazy as _


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'delivery_type', 'delivery_price', 'city', 'paid', 'created', 'updated', 'payment_type']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['id', 'user__email', 'user__full_name', 'city', 'address']
    save_on_top = True
    inlines = [OrderItemInline]

    fieldsets = (
        (_('Информация о пользователе'), {
            'fields': ('user', ),
            'description': _('Информация о пользователе')
        }),
        (_('Платёжная информация'), {
            'fields': ('payment_type', 'card_number', 'status', 'payment_code', 'paid'),
            'description': _('Платёжная информация')
        }),
        (_('Информация о доставке'), {
            'fields': ('delivery_type', 'delivery_price', 'city', 'address'),
            'description': _('Информация о доставке'),
            'classes': ['collapse']
        }),
    )


admin.site.register(Order, OrderAdmin)
