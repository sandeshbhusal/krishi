from django.db import models

# Create your models here.
class Crops(models.Model):
    cropName     = models.CharField(max_length = 30)
    altitude     = models.IntegerField()
    humidity     = models.IntegerField()
    temperature  = models.FloatField()
    manpower     = models.CharField(max_length = 100)
    fertilizer   = models.CharField(max_length = 100)
    insecticides = models.CharField(max_length = 50)
    pesticides   = models.CharField(max_length = 50)
    investment   = models.CharField(max_length = 50)
    turnover     = models.CharField(max_length = 50)
    breakeven    = models.CharField(max_length = 50)
    places       = models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'Crop'
        verbose_name_plural = 'Crops'


    def __str__(self):
        return self.cropName

