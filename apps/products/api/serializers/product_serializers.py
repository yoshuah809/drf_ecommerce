from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, ProductCategorySerializer

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
  # First Way to serialize related properties
  # measure_unit = MeasureUnitSerializer()      
  # category_product = ProductCategorySerializer()

  # Second Way to serialize related properties
  # measure_unit = serializers.StringRelatedField()      
  #category_product = serializers.StringRelatedField()  


  class Meta:
      model = Product
      exclude = ('active', 'date_created', 'date_modified', 'date_deleted')
    # Third Way to serialize related properties
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'name': instance.name,
      'description': instance.description,
      'image': instance.image if instance.image != '' else '',
      'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
      'category_product': instance.category_product.description if instance.category_product is not None else '',
    }