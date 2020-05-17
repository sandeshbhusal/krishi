from rest_framework import serializers
from .models import Crops

class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Crops
        # fields = ('lineName','image','details',)
        fields = ('cropName','minAltitude', 'maxAltitude', 'humidity', 'temperature','manpower', 'fertilizer', 'insecticides', 'pesticides', 'investment', 'turnover', 'breakeven', 'places',)

