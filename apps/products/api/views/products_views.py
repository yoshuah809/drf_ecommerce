from rest_framework.response import Response
from apps.base.api import GeneralListApiView
from rest_framework import generics, status

from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer


class ProductCreateApiView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(active = True)


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(active = True)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()    
        if product:
            product.active = False
            product.save()
            return Response({'message': 'Product has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Product Not Found, Please Try a diferent id'}, status=status.HTTP_404_NOT_FOUND)