from django.contrib import admin
from app_orders.models import OrderItem, Order
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'delivery_type', 'delivery_price', 'get_total_cost', 'paid', 'payment_type', 'city', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['id', 'user__email', 'user__full_name', 'city', 'address']
    save_on_top = True
    inlines = [OrderItemInline]

    def get_total_cost(self, obj):
        total_cost = float(sum(item.get_cost() for item in obj.items.all()) + obj.delivery_price)
        return Decimal.from_float(total_cost).quantize(Decimal("1.00"))

    get_total_cost.short_description = _('итоговая стоимость')

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
