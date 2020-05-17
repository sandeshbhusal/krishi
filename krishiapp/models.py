from django.db import models

# Create your models here.
class Crops(models.Model):
    cropName     = models.CharField(max_length = 30)
    minAltitude  = models.IntegerField()
    maxAltitude  = models.IntegerField()
    humidity     = models.FloatField()
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

    def distance(self, yourAltitude, yourTemperature, yourHumidity):
        avgalt          = (self.minAltitude + self.maxAltitude)/2
        normalt         = (avgalt - 10)/(4000-10)
        normtemp        = (self.temperature + 1)/(42 + 1)
        normhum         = (self.humidity -25)/(65 - 25)
        yourAltitude    = (yourAltitude - 10)/(4000-10)
        yourHumidity    = (yourHumidity -25)/(65-25)
        yourTemperature = (yourTemperature +1)/(42 +1)
        dist            = 1 * (normalt - yourAltitude)**2 + 1 * (normtemp - yourTemperature)**2 + 1* (normhum - yourHumidity)**2
        return dist
