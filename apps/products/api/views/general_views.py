from django.shortcuts import render
from rest_framework import generics

from apps.products.models import ProductCategory, MeasureUnit, OnSaleIndicator
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, OnSaleIndicatorSerializer, ProductCategorySerializer

# Create your views here.

class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(active=True)


class IndicatorListAPIView(generics.ListAPIView):
    serializer_class = OnSaleIndicatorSerializer

    def get_queryset(self):
        return OnSaleIndicator.objects.filter(active=True)


class ProductCategoryListAPIView(generics.ListAPIView):
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        return ProductCategory.objects.filter(active=True)        