from django.shortcuts import render
import requests

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from rest_framework import generics
from rest_framework import permissions
from .models import Crops
from .serializers import CropSerializer

class cropList(generics.ListCreateAPIView):
    queryset = Crops.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        youralt  = int(self.request.query_params.get('altitude', None))
        yourtemp = int(self.request.query_params.get('temperature', None))
        yourhum  = int(self.request.query_params.get('humidity', None))
        queryset = Crops.objects.all()
        queryset = sorted( queryset, key= lambda t:t.distance(youralt, yourtemp, yourhum))
        return queryset

class cropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Crops.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# Create your views here.
# def indexView(request):
#     return render(request, "index.html", {})

=======

# Create your views here.

def indexView(request):
    return render(request, "index.html", {})

def secondPage(request, *args, **kwargs):
    # This view returns the second page.
    # The second page contains information regarding the current location.

    lat = (request.GET.get("latitude"))
    lng = (request.GET.get("longitude"))
    alt = (request.GET.get("altitude"))
    
    print(lat, lng, alt)
    
    # Get current temperature, wind and humidity
    weatherApi = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=0a52ba8dcd307d969881a23864a6230e"
    # Make a request and decode json data from api 
    resp = requests.get(weatherApi)
    weatherData = resp.json()
    print(weatherData)
    data = {
        "location": weatherData.get("name"),
        "humidity": weatherData.get("main").get("humidity"),
        "wind": weatherData.get("wind").get("speed"),
        "descriptionOfWeather": weatherData.get("weather")[0].get("description"),
        "temperature": (float(weatherData.get("main").get("temp")) / 10),

    }
    return render(request, "apiCallAndScan.html", context={"data": data})
  
# def showCropsList(request):
# 	#PRASANGA --- CROPS HERE HAI !! 
# 	crops =[{"name":"rice" , "altitude":20, "temperature":10, "humidity": 5}, 
# 			{"name":"wheat", "altitude":30, "temperature":5, "humidity": 52},
# 			{"name":"barley" , "altitude":10, "temperature":-10, "humidity": 5}]

# 	return render(request, "cropslist.html", {'crops':crops})

