from django.shortcuts import render
import requests

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
	#PRASANGA --- CROPS HERE HAI !! 
	crops =[{"name":"rice" , "altitude":20, "temperature":10, "humidity": 5}, 
			{"name":"wheat", "altitude":30, "temperature":5, "humidity": 52},
			{"name":"barley" , "altitude":10, "temperature":-10, "humidity": 5}]

	return render(request, "cropslist.html", {'crops':crops})

