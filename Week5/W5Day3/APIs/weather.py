import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from securityCheck import safe_request



WEATHER_KEY = os.getenv('WEATHER_API')

def set_url():
    load_dotenv('C:/Users/jaykp/Desktop/Devstree Task/Week5/W5Day3/allAPI.env')
    
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
    API_KEY = os.getenv('WEATHER_API')

    if not API_KEY:
        print("Error: API key not found in allApi.env")
        exit()

    city_name = input("Enter city name: ").capitalize()
    url = f'{BASE_URL}appid={API_KEY}&q={city_name}'
    return url,city_name

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return round(celsius, 2), round(fahrenheit, 2)

def set_weather_info(data):
    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temp_c, temp_f = kelvin_to_celsius_fahrenheit(data['main']['temp'])
    temp_c_feels_like, temp_f_feels_like = kelvin_to_celsius_fahrenheit(data['main']['feels_like'])
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    speed = data['wind']['speed']
    country = data['sys']['country']
    offset = timedelta(seconds=data['timezone'])
    sunrise = datetime.fromtimestamp(data['sys']['sunrise'], tz=timezone.utc) + offset
    sunset = datetime.fromtimestamp(data['sys']['sunset'], tz=timezone.utc) + offset
    
    return {
        "city_name": data['name'],
        "weather": weather,
        "description": description, 
        "temp_c": temp_c,
        "temp_f": temp_f,   
        "temp_c_feels_like": temp_c_feels_like,
        "temp_f_feels_like": temp_f_feels_like,
        "pressure": pressure, 
        "humidity": humidity,
        "speed": speed,
        "country": country,
        "sunrise": sunrise,
        "sunset": sunset
    }
    
def print_info(info):
    print(f'City Name: {info["city_name"]}')
    print(f'Weather: {info["weather"]}')
    print(f'Description: {info["description"]}')
    print(f'Temperature: {info["temp_c"]} °C / {info["temp_f"]} °F')
    print(f'Feels Like: {info["temp_c_feels_like"]} °C / {info["temp_f_feels_like"]} °F')
    print(f'Pressure: {info["pressure"]} hPa')
    print(f'Humidity: {info["humidity"]}%')
    print(f'Wind Speed: {info["speed"]} m/s')
    print(f'Country: {info["country"]}')
    print(f'Sunrise: {info["sunrise"]}')
    print(f'Sunset: {info["sunset"]}')
    
value_url,city_name = set_url() 
data = safe_request(value_url)
if data is None:
    print("Failed to fetch weather data after multiple attempts.")
    exit()

if __name__ == "__main__":    
    set_weather_info(data)
    print_info(set_weather_info(data))


