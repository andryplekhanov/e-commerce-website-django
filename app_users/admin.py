from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, ProxyGroups
from django.utils.translation import gettext_lazy as _


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'full_name', 'date_joined', 'is_active', 'is_staff']
    list_filter = ['is_active', 'is_staff', 'date_joined']
    search_fields = ['id', 'email', 'full_name']
    save_on_top = True
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_active.short_description = _('активировать')
    make_inactive.short_description = _('деактивировать')


admin.site.unregister(Group)
admin.site.register(ProxyGroups)
admin.site.register(User, UserAdmin)
