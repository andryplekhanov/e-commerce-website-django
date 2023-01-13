from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from app_product.models import *


class ParameterValueInline(admin.TabularInline):
    model = Parameter


class ImageInline(admin.TabularInline):
    fk_name = 'product'
    model = Image


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'vendor', 'created', 'updated']
    list_filter = ['category', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageInline, ParameterValueInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Parameter)
admin.site.register(ParameterName)
admin.site.register(ParameterValue)