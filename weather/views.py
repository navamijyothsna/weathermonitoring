import requests
from django.shortcuts import render
def home(request):
    print("VIEW CALLED")
import requests
from django.shortcuts import render

def home(request):
    weather_list = []
    error = None

    if request.method == "POST":
        cities = request.POST.get('city')
        api_key = "ba0fa6e672334611dbff6f3f4e809e20"

        city_list = [city.strip() for city in cities.split(",")]

        for city in city_list:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_list.append({
                    "city": city,
                    "temperature": data['main']['temp'],
                    "humidity": data['main']['humidity'],
                    "description": data['weather'][0]['description'],
                    "icon": data['weather'][0]['icon']
                })
            else:
                error = f"Could not fetch weather for {city}"

    return render(request, "weather/home.html", {"weather_list": weather_list, "error": error})

from django.shortcuts import render

def satellites(request):
    satellite_data = [
        {
            "name": "INSAT-3D",
            "launch": "2013",
            "purpose": "Weather Monitoring",
            "orbit": "Geostationary",
        },
        {
            "name": "Cartosat-3",
            "launch": "2019",
            "purpose": "High Resolution Imaging",
            "orbit": "Sun-Synchronous",
        },
        {
            "name": "Oceansat-2",
            "launch": "2009",
            "purpose": "Ocean Surface Study",
            "orbit": "Polar",
        },
    ]

    return render(request, "satellites.html", {"satellites": satellite_data})