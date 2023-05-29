from rest_framework import serializers
from .models import *


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('slug',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('slug',)


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('slug',)


class WarrantyPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyPeriod
        fields = ('id', 'type', 'slug',)
        read_only_fields = ('slug',)


class ProductSerializer(serializers.ModelSerializer):
    brand = ProductBrandSerializer(read_only=True)
    category = ProductCategorySerializer(read_only=True)
    type = ProductTypeSerializer(read_only=True)
    warranty = WarrantyPeriodSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'price', 'description', 'image', 'stock',
                  'category', 'type', 'brand', 'warranty', 'is_available', 'created_at',)
        read_only_fields = ('slug',)
