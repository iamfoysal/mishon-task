from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import *
from .serializer import *


class ProductCategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['slug']
