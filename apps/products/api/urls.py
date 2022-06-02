from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListCreateAPIView, IndicatorListAPIView, ProductCategoryListCreateAPIView
from apps.products.api.views.products_views import ProductListCreateAPIView, ProductRetrieveAPIView,ProductDestroyAPIView, ProductUpdateAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListCreateAPIView.as_view(), name='measure_unit'),
    path('onsale_indicator/', IndicatorListAPIView.as_view(), name='onsale_indicator'),
    path('product_category/', ProductCategoryListCreateAPIView.as_view(), name='product_category'),
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('product_get/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_get'),
    path('product_delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
    path('product_update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
   
]
