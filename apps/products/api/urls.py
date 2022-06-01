from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, ProductCategoryListAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('onsale_indicator/', IndicatorListAPIView.as_view(), name='onsale_indicator'),
    path('product_category/', ProductCategoryListAPIView.as_view(), name='product_category'),
   
]
