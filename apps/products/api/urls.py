from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, ProductCategoryListAPIView
from apps.products.api.views.products_views import ProductListApiView, ProductCreateApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('onsale_indicator/', IndicatorListAPIView.as_view(), name='onsale_indicator'),
    path('product_category/', ProductCategoryListAPIView.as_view(), name='product_category'),
    path('product_list/', ProductListApiView.as_view(), name='product_list'),
    path('product_create/', ProductCreateApiView.as_view(), name='product_create'),
   
]
