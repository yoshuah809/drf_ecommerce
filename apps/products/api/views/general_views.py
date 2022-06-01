from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, OnSaleIndicatorSerializer, ProductCategorySerializer

# Create your views here.

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer

  
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = OnSaleIndicatorSerializer


class ProductCategoryListAPIView(GeneralListApiView):
    serializer_class = ProductCategorySerializer

     