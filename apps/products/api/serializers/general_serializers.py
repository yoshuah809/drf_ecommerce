from apps.products.models import MeasureUnit, ProductCategory, OnSaleIndicator

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('active','date_created', 'date_modified', 'date_deleted')


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        exclude = ('active','date_created', 'date_modified', 'date_deleted')


class OnSaleIndicatorSerializer(serializers.ModelSerializer):        
    class Meta:
        model = OnSaleIndicator
        exclude = ('active','date_created', 'date_modified', 'date_deleted')