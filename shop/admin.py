from django.contrib import admin
from .models import Product, ProductCategory, ProductBrand, ProductType, WarrantyPeriod


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (None, {
            'fields': ('name', 'slug',)
        }),
    )


class WarrantyPeriodAdmin(admin.ModelAdmin):
    list_display = ('type', 'slug',)
    prepopulated_fields = {'slug': ('type',)}

    fieldsets = (
        (None, {
            'fields': ('type', 'slug',)
        }),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock',)
    list_filter = ('available', 'created', 'updated',)








admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(WarrantyPeriod, WarrantyPeriodAdmin)
