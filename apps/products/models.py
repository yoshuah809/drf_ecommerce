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
        