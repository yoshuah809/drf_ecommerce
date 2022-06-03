from rest_framework.response import Response
from rest_framework import generics, status,viewsets
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, OnSaleIndicatorSerializer, ProductCategorySerializer

# Create your views here.

class MeasureUnitViewsets(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(active = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, active = True).first()  

  
class IndicatorViewsets(viewsets.ModelViewSet):
    serializer_class = OnSaleIndicatorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(active = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, active = True).first()  

class ProductCategoryViewsets(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
   
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(active = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, active = True).first()  

     