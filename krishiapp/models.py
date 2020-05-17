from django.db import models

# Create your models here.
class Crops(models.Model):
    cropName     = models.Charfield(max_length = 30)
    altitude     = models.IntegerField()
    humidity     = models.IntegerField()
    temperature  = models.FloatField()
    manpower     = models.Charfield(max_length = 100)
    fertilizer   = models.Charfield(max_length = 100)
    insecticides = models.Charfield(max_length = 50)
    pesticides   = models.Charfield(max_length = 50)
    investment   = models.Charfield(max_length = 50)
    turnover     = models.Charfield(max_length = 50)
    breakeven    = models.Charfield(max_length = 50)
    places       = models.Charfield(max_length=2000)

    class Meta:
        verbose_name = 'Crop'
        verbose_name_plural = 'Crops'


    def __str__(self):
        return self.cropName

