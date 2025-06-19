from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):
    # Default city if none is provided
    city = request.POST.get('city', 'gwalior')

    # OpenWeather API URL
    weather_url = f'https://api.openweathermap.org/data/2.5/weather'
    weather_params = {'q': city, 'appid': 'f6bb2b793a86f304f1a455849a32c622', 'units': 'metric'}

    # Google Custom Search API URL
    API_KEY = 'AIzaSyDQbdtSWqvWgR0lwINInRGeo_0BQT8DEZM'
    SEARCH_ENGINE_ID = 'e51c95ae4ea3e4e84'
    search_query = f"{city} 1920x1080"
    search_params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': search_query,
        'searchType': 'image',
        'imgSize': 'xlarge',
        'start': 1,
    }
    search_url = "https://www.googleapis.com/customsearch/v1"

    try:
        # Fetch weather data
        weather_response = requests.get(weather_url, params=weather_params).json()
        description = weather_response['weather'][0]['description']
        icon = weather_response['weather'][0]['icon']
        temp = weather_response['main']['temp']
        day = datetime.date.today()

        # Fetch image data
        image_response = requests.get(search_url, params=search_params).json()
        search_items = image_response.get("items")
        image_url = search_items[1]['link'] if search_items and len(search_items) > 1 else None

        # Fallback image if no image is found
        if not image_url:
            image_url = "https://via.placeholder.com/1920x1080?text=No+Image+Available"

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url,
        })

    except KeyError as e:
        # Handle API response issues
        messages.error(request, 'Error fetching data. Showing default values.')
        fallback_city = 'gwalior'
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': datetime.date.today(),
            'city': fallback_city,
            'exception_occurred': True,
            'image_url': "https://via.placeholder.com/1920x1080?text=Fallback+City",
        })
