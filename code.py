import requests
from pprint import pprint

API_Key = '' # You can put an API key generated on openweathermap.org

city = input('Insira a Cidade: ')

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_Key+"&lang=pt_BR&units=metric"

weather_data = requests.get(base_url).json()

pprint(weather_data)