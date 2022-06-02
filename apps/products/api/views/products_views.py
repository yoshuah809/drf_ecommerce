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