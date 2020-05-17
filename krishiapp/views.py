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
  
def showCropsList(request):
	return render(request, "cropslist.html", {})

def cropDetails(request, cropid):
    # Whatever the cropid, we need its data from the database.
    # Uncomment these lines when done.
    # crop = models.Crops.get(id=cropid)

    

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

    return render(request, "cropdetails.html", {"map_": m._repr_html_()})