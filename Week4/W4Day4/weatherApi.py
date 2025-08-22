import requests
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import os

def set_url():
    load_dotenv("weatherApi.env")
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
    API_KEY = os.getenv('WEATHER_API')

    if not API_KEY:
        print("Error: API key not found in weatherApi.env")
        exit()

    city_name = input("Enter city name: ").capitalize()
    url = f'{BASE_URL}appid={API_KEY}&q={city_name}'
    return url, city_name

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return round(celsius, 2), round(fahrenheit, 2)

def set_weather_info(response):
    temp_c, temp_f = kelvin_to_celsius_fahrenheit(response['main']['temp'])
    feel_c, feel_f = kelvin_to_celsius_fahrenheit(response['main']['feels_like'])

    humidity = response['main']['humidity']
    pressure = response['main']['pressure']
    weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    wind_speed = response['wind']['speed']

    offset = timedelta(seconds=response['timezone'])
    sunrise = datetime.fromtimestamp(response['sys']['sunrise'], tz=timezone.utc) + offset
    sunset = datetime.fromtimestamp(response['sys']['sunset'], tz=timezone.utc) + offset
    country = response['sys']['country']

    return {
        "temp_c": temp_c,
        "temp_f": temp_f,
        "feel_c": feel_c,
        "feel_f": feel_f,
        "humidity": humidity,
        "pressure": pressure,
        "weather": weather,
        "description": description,
        "wind_speed": wind_speed,
        "sunrise": sunrise,
        "sunset": sunset,
        "country": country
    }

def print_weather_info(city_name, info):
    """Display weather details."""
    print(f"Weather in {city_name}, {info['country']}")
    print(f"Temperature: {info['temp_c']}°C / {info['temp_f']}°F")
    print(f"Feels Like: {info['feel_c']}°C / {info['feel_f']}°F")
    print(f"Condition: {info['weather']} - {info['description']}")
    print(f"Wind speed: {info['wind_speed']} m/s")
    print(f"Humidity: {info['humidity']}%")
    print(f"Pressure: {info['pressure']} hPa")
    print(f"Sunrise: {info['sunrise']}")
    print(f"Sunset: {info['sunset']}")

# Main flow
url, city_name = set_url()
response = requests.get(url).json()

if response.get("cod") != 200:
    print("Error:", response.get("message", "Unknown error"))
else:
    weather_info = set_weather_info(response)
    print_weather_info(city_name, weather_info)
