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
    response = requests.get(api_url)
    weather_data = response.json()
    return weather_data
