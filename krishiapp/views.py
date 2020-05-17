from django.shortcuts import render
from . import models
import requests
import geocoder
import folium

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
  
# TODO: Change the api specification here.
def showCropsList(request):
	#PRASANGA --- CROPS HERE HAI !!
    youralt  = 2000
    yourtemp = 30
    yourhum  = 40
    queryset = Crops.objects.all()
    # queryset = sorted( queryset, key= lambda t:t.distance(youralt, yourtemp, yourhum))
    crops = []
    for item in queryset:
        crops.append({"name":item.cropName, "altitude":(item.minAltitude + item.maxAltitude)//2, "temperature":item.temperature, "humidity":item.humidity})
    # crops =[{"name":"rice" , "altitude":20, "temperature":10, "humidity": 5}, 
    # 		{"name":"wheat", "altitude":30, "temperature":5, "humidity": 52},
    # 		{"name":"barley" , "altitude":10, "temperature":-10, "humidity": 5}]

    return render(request, "cropslist.html", {'crops':crops})

def cropDetails(request, cropid):
    # Whatever the cropid, we need its data from the database.
    # Uncomment these lines when done.
    crop = models.Crops.objects.get(pk=cropid)

    # Get the crop details.
    detailDict = {
        "cropName": crop.cropName or  "apple",
        "altitude": crop.altitude or  "100ft",
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
    countries = ['Nepal', 'India', 'Bhutan', 'Greece', 'Norway', 'Brazil', 'Chile', 'Canada']
    m = folium.Map(location = [0, 0], zoom_start = 1)
    # Start reverse geocoding countries and put markers on map.
    for country in countries:
        # Reverse geocode:
        api = f"http://api.positionstack.com/v1/forward?access_key=391ce60377e3a2b284675d583b2b703b&query={country}"
        response = requests.get(api)
        json = response.json()
        # Search json items
        for result in json.get("data"):
            if result['name'] == result['country']:
                folium.Marker([result['latitude'], result['longitude']], popup = f'{country}').add_to(m)
                break

    return render(request, "cropdetails.html", {"map_": m._repr_html_(), "data": detailDict})