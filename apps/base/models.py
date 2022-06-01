from django.db import models

# Create your models here.
class BaseModel(models.model):

    id = models.AutoField(primary_key=True)
    active = models.BooleanField('Active', default = True)
    date_created = models.DateField('Date Created', auto_now=False, auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True, auto_now_add=False)
    date_deleted = models.DateField('Date Deleted', auto_now=True, auto_now_add=False)


    class Meta:
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
