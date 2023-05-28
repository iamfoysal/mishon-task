from rest_framework import serializers
from .models import Product, ProductBrand, ProductCategory, ProductType, WarrentyPeriod

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'slug',)

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class WarrentyPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrentyPeriod
        fields = '__all__'
