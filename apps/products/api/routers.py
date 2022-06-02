from rest_framework.routers import DefaultRouter
from apps.products.api.views.products_viewsets import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, 'Products')

urlpatterns = router.urls