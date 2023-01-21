from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from app_review.models import Review
from django.utils.translation import gettext_lazy as _


@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_users_full_name', 'get_short_text', 'link_to_product', 'created']
    list_filter = ['created']
    search_fields = ['text', 'product__name', 'user__email', 'user__full_name']
    save_on_top = True

    def get_short_text(self, obj):
        if len(obj.text) <= 50:
            return obj.text
        return f'{obj.text[:50]}...'

    get_short_text.short_description = _('текст комментария')

    def get_users_full_name(self, obj):
        if len(obj.user.full_name) <= 30:
            return f'{obj.user.full_name}'
        return f'{obj.user.full_name[:30]}...'

    get_users_full_name.short_description = _('ФИО')

    def link_to_product(self, obj):
        link = reverse("admin:app_product_product_change", args=[obj.product_id])
        return format_html('<a href="{}">Edit {}</a>', link, obj.product.name)

    link_to_product.short_description = _('товар')
