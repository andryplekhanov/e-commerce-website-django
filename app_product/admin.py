from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from app_product.models import *


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


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'value', ]
    list_filter = ['parameter']
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ParameterName)
admin.site.register(ParameterValue)
