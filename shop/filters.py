from django_filters import FilterSet, CharFilter, NumberFilter
from django.db.models import Q
from .models import Product


class ProductFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr='exact')
    slug = CharFilter(field_name='slug', lookup_expr='icontains')
    brand = CharFilter(field_name='brand__slug',
                       lookup_expr='icontains', method='filter_by_multiple_brands')
    category = CharFilter(field_name='category__slug',
                          lookup_expr='icontains', method='filter_by_multiple_categories')
    type = CharFilter(field_name='type__slug', lookup_expr='icontains')
    warranty = CharFilter(field_name='warranty__slug', lookup_expr='icontains')

    def filter_by_multiple_categories(self, queryset, name, value):
        categories = value.split(',')
        query = Q()
        for category in categories:
            query |= Q(**{f'{name}__icontains': category.strip()})
        return queryset.filter(query)

    def filter_by_multiple_brands(self, queryset, name, value):
        brands = value.split(',')
        query = Q()
        for brand in brands:
            query |= Q(**{f'{name}__icontains': brand.strip()})
        return queryset.filter(query)

    class Meta:
        model = Product
        fields = ('id', 'slug', 'brand', 'category', 'type', 'warranty',)
