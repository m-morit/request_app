from django.shortcuts import render
import requests

def index(request):
    return render(request,'request/index.html')

def get_weather(request):
    if request.method == 'POST':
        selected_location = request.POST.get('location')
        weather_data = fetch_weather(selected_location)
        return render(request,'request/weather.html',{'weather_data': weather_data})
    else:
        return render(request,'request/index.html')
    
def fetch_weather(location):
    
    api_url = f'https://weather.tsukumijima.net/api/forecast?city={location}'
    city_ids = {"Osaka":"270000",
                "Kyoto":"260010",
                "Kobe":"280010",}
    city_id = city_ids.get(location, "270000") 
    params = {"city": city_id}
    response = requests.get(api_url, params=params)
    weather_data = response.json()
    print(weather_data["forecasts"][0])
    weather_data["forecast"] = weather_data["forecasts"][0]
    return weather_data
