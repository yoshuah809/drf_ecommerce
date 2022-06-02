from rest_framework.response import Response
from rest_framework import generics, status
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, OnSaleIndicatorSerializer, ProductCategorySerializer

# Create your views here.

class MeasureUnitListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.filter(active = True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = OnSaleIndicatorSerializer


class ProductCategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategorySerializer.Meta.model.objects.filter(active = True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



     