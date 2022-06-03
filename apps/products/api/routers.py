from rest_framework.routers import DefaultRouter
from apps.products.api.views.products_viewsets import ProductViewSet
from apps.products.api.views.general_views import *


router = DefaultRouter()
router.register(r'products', ProductViewSet, 'Products')
router.register(r'measure_unit', MeasureUnitViewsets, 'measure_unit')
router.register(r'onsale_indicators', IndicatorViewsets, 'onsale_indicators')
router.register(r'category_products', ProductCategoryViewsets, 'category_products')

urlpatterns = router.urls

