from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import *
from .serializer import *
from .filters import *


class ProductCategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductBrandViewset(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer


class ProductTypeViewset(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class WarrantyPeriodViewset(viewsets.ModelViewSet):
    queryset = WarrantyPeriod.objects.all()
    serializer_class = WarrantyPeriodSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
    http_method_names = ['get']
