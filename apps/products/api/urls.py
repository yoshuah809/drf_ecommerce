from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListCreateAPIView, IndicatorListAPIView, ProductCategoryListCreateAPIView
from apps.products.api.views.products_viewsets import ProductListCreateAPIView, ProductRetrieveUpdateAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListCreateAPIView.as_view(), name='measure_unit'),
    path('onsale_indicator/', IndicatorListAPIView.as_view(), name='onsale_indicator'),
    path('product_category/', ProductCategoryListCreateAPIView.as_view(), name='product_category'),
   
]
