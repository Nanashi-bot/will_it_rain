import requests
import geocoder
from dotenv import load_dotenv
import os

load_dotenv()
API = os.getenv("API_KEY")

g = geocoder.ip('me')
#print(g.latlng)
#params = {'lat': g.latlng[0], 'long': g.latlng[1], 'appid': API}
response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={g.latlng[0]}&lon={g.latlng[1]}&appid={API}')
#response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)

for i in range(4):
    print(response.json()['list'][i]['main']['temp'])
    print(response.json()['list'][i]['weather'][0]['main'])
    print(response.json()['list'][i]['weather'][0]['description'])
    print(response.json()['list'][i]['weather'][0]['icon'])
    a = response.json()['list'][i]['weather'][0]['main'].lower()
    print(response.json()['list'][i][a])
    print(response.json()['list'][i]['dt_txt'])
    print("\n\n\n")
