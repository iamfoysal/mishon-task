from rest_framework.routers import DefaultRouter
from .views import *



router= DefaultRouter()

router.register('categories', ProductCategoryViewset, basename='categories')












urlpatterns = router.urls