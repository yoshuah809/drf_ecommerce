from rest_framework.response import Response
from apps.base.api import GeneralListApiView
from rest_framework import generics, status, viewsets, permissions

from apps.products.api.serializers.product_serializers import ProductSerializer

#ViewSets Implementation
class ProductViewSet(viewsets.ModelViewSet):
    """
    Product End Point
    """
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(active = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, active = True).first()  
    
    def list(self, request):
        """
        Product End Point to List all Products-2
                

        Params--->
        No parameters needed
        """ 
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
   

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Response({'error': "Product not found"}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()    
        if product:
            product.active = False
            product.save()
            return Response({'message': 'Product has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Product Not Found, Please Try a diferent id'}, status=status.HTTP_404_NOT_FOUND)

#generics.ListCreateAPIView Implementation
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(active = True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if type(pk) == str:
            return('Please Enter a Valid Id')    
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(active = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, active = True).first()    

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status =status.HTTP_200_OK)
        Response({'error': "Product not found"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Response({'error': "Product not found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()    
        if product:
            product.active = False
            product.save()
            return Response({'message': 'Product has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Product Not Found, Please Try a diferent id'}, status=status.HTTP_404_NOT_FOUND)

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
