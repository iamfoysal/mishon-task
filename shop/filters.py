from django_filters import (FilterSet,
                            CharFilter,
                            NumberFilter,
                            )
from django.db.models import Q
from .models import Product


class ProductFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr='exact')
    slug = CharFilter(field_name='slug', lookup_expr='icontains')
    brand = CharFilter(field_name='brand__slug', lookup_expr='icontains')
    category = CharFilter(field_name='category__slug', lookup_expr='icontains')
    type = CharFilter(field_name='type__slug', lookup_expr='icontains')
    warranty = CharFilter(field_name='warranty__slug', lookup_expr='icontains')
    

    class Meta:
        model = Product
        fields = ('id', 'slug', 'brand', 'category', 'type', 'warranty',)
