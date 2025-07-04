from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'gwalior'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=enter app api'
    PARAMS = {'units': 'metric'}

    API_KEY = 'enter your api'
    SEARCH_ENGINE_ID = 'enter your search engine'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    try:
        image_data = requests.get(city_url).json()
        search_items = image_data.get("items", [])
        image_url = search_items[1]['link'] if len(search_items) > 1 else None
    except (requests.exceptions.RequestException, KeyError, IndexError):
        image_url = None  # Default to None if any error occurs

    try:
        data = requests.get(url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })
    except (requests.exceptions.RequestException, KeyError):
        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')
        city = 'gwalior'
        fallback_data = requests.get(url, params=PARAMS).json()
        description = fallback_data.get('weather', [{}])[0].get('description', 'clear sky')
        icon = fallback_data.get('weather', [{}])[0].get('icon', '01d')
        temp = fallback_data.get('main', {}).get('temp', 25)
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': 'indore',
            'exception_occurred': exception_occurred,
            'image_url': image_url
        })
