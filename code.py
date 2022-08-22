import requests
from pprint import pprint

API_Key = 'a93ceabab06761ba48d37d5fa852d393'

city = input('Insira a Cidade: ')

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_Key+"&lang=pt_BR&units=metric"

weather_data = requests.get(base_url).json()

pprint(weather_data)