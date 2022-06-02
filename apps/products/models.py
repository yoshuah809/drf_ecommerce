from pyexpat import model
from unittest.main import MODULE_EXAMPLES
from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    historical= HistoricalRecords()

    @property 
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value    

    class Meta:
        verbose_name='MeasureUnit'  
        verbose_name_plural='MeasureUnits'  

    def __str__(self):
        return self.description    


class ProductCategory(BaseModel):
    description = models.CharField('Description',max_length=50, blank=False, null=False, unique=True)
    historical= HistoricalRecords()

    @property 
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value   

    class Meta:
      verbose_name='ProductCategory'  
      verbose_name_plural='ProductCategories'  

    def __str__(self):
        return self.description    

class OnSaleIndicator(BaseModel):
    discount_value= models.SmallIntegerField(default = 0)
    category_product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='On Sale Indicator')
    historical= HistoricalRecords()
    
    @property 
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value   

    class Meta:
      verbose_name='On Sale Indicator'  
      verbose_name_plural='On Sale Indicators' 

    def __str__(self):
       return f'Discount{self.category_product}:{self.discount_value}%'     

class Product(BaseModel):
    name = models.CharField('Product Name', max_length=150, blank=False, null=False, unique=True)
    description = models.TextField('Product Description', blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Measure Unit', default=1)
    category_product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Product Category', null= True, default=1)
    image = models.ImageField('Product Image', upload_to='products/', blank=True, null=True)
    historical= HistoricalRecords()

    @property 
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value   

    class Meta:
      verbose_name='Product'  
      verbose_name_plural='Products' 

    def __str__(self):
        return self.name