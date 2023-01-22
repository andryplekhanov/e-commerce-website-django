from django.contrib import admin
from django.db.utils import ProgrammingError
from app_settings.models import SiteSettings


class SiteSettingsAdmin(admin.ModelAdmin):
    """ В админ-панели нужно создать экземпляр с настройками """

    def has_add_permission(self, request, obj=None):
        """ Запрещает создать более 1го экземпляра с настройками """
        if not self.model.objects.all():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """ Запрещает удалять экземпляр с настройками """
        return False


admin.site.register(SiteSettings, SiteSettingsAdmin)
