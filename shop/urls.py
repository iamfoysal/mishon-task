from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('categories', ProductCategoryViewset, basename='categories')
router.register('brands', ProductBrandViewset, basename='brands')
router.register('types', ProductTypeViewset, basename='types')
router.register('warranty-periods', WarrantyPeriodViewset,
                basename='warranty-periods')
router.register('products', ProductViewset, basename='products')

urlpatterns = router.urls
