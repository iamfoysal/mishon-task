from django.contrib import admin

# Register your models here.
from .models import Product, ProductCategory, ProductBrand, ProductType, WarrentyPeriod

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductCategory, CategoryAdmin)
