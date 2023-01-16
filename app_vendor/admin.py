from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Vendor, VendorAdmin)
