from django.shortcuts import render
from . import models
import requests
import geocoder
import pandas as pd
import folium

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from rest_framework import generics
from rest_framework import permissions
from .models import Crops
from .serializers import CropSerializer
from .apikeys import * 
# TODO: Implement Apikeys in a different file and use this app! 
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
    weatherApi = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_KEY_OPENWEATHER}"
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
  
def showCropsList(request):
    # Get the params from Url.
    youralt  = request.GET.get("altitude")
    yourtemp = request.GET.get("temperature")
    yourhum  = request.GET.get("humidity")
    print("Cropslist received: ", youralt, yourtemp, yourhum)
    queryset = Crops.objects.all()[:7]
    # queryset = sorted( queryset, key= lambda t:t.distance(youralt, yourtemp, yourhum))
    crops = []
    for item in queryset:
        crops.append({"id":item.pk, "name":item.cropName, "altitude":(item.minAltitude + item.maxAltitude)//2, "temperature":item.temperature, "humidity":item.humidity})
	
    return render(request, "cropslist.html", {'crops':crops})

    # crops =[{"name":"rice" , "altitude":20, "temperature":10, "humidity": 5}, 
	# 		{"name":"wheat", "altitude":30, "temperature":5, "humidity": 52},
	# 		{"name":"barley" , "altitude":10, "temperature":-10, "humidity": 5}]

	
def cropDetails(request, cropid):
    # Whatever the cropid, we need its data from the database.
    # Uncomment these lines when done.
    crop = models.Crops.objects.get(pk=cropid)

    # Get the crop details.
    detailDict = {
        "cropName": crop.cropName or  "apple",
        "altitude": crop.minAltitude or  "100ft",
        "altitude": crop.maxAltitude or  "3000ft",
        "humidity": crop.humidity or  "20",
        "temperature": crop.temperature or  "10*C",
        "manpower": crop.manpower or  "10 people",
        "fertilizer": crop.fertilizer or  "100KG",
        "insecticides": crop.insecticides or  "Some pesticide",
        "pesticides": crop.pesticides or  "Some pesticide",
        "investment": crop.investment or  "NRs. 100,000",
        "turnover": crop.turnover or  "NRs. 200,000",
        "breakeven": crop.breakeven or  "200 KG"
    }

    places = crop.places

    countries = places.split(",")

    # This section is purely for the map.
    # Crop growing countries:
    m = folium.Map(location = [0, 0], zoom_start = 1)
    # Start reverse geocoding countries and put markers on map.

    # for country in countries:
    #     # Reverse geocode:
    #     api = f"http://api.positionstack.com/v1/forward?access_key={API_KEY_POSITIONSTACK}&query={country}"
    #     response = requests.get(api)
    #     json = response.json()
    #     # Search json items
    #     for result in json.get("data"):
    #         if result['name'] == result['country']:
    #             folium.Marker([result['latitude'], result['longitude']], popup = f'{country}').add_to(m)
    #             break

    # Alternate version: Pandas to the rescue!
    import pandas as pd
    import os
    df = pd.read_csv(os.path.join(os.path.split(__file__)[0], "countries.csv"))
    for country in countries:
        try:
            row = df.loc[df['name'] == country]
            lat = (row['latitude'].iloc[0])
            lon = (row['longitude'].iloc[0])
            print("--------", lat, lon)
            folium.Marker([lat, lon], popup = f'{country}').add_to(m)
        except:
            # SOme countries' data is not in csv file :(
            print("invalid for ", country)
            pass
        
    return render(request, "cropdetails.html", {"map_": m._repr_html_(), "data": detailDict})
