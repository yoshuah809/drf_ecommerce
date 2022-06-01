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
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Measure Unit')
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

class OnSaleInicator(BaseModel):
    discount_value= models.SmallIntegerField(default = 0)
    category_product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='On Sale Inicator')
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

    