from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

def getWeather():
    
    apikey = "apikey=" + os.getenv("CLIMACELL_APIKEY")

    url = "https://api.climacell.co/v3/weather/realtime?lat=41.574&lon=-93.707&unit_system=us&fields=temp,feels_like,weather_code,humidity,wind_speed,wind_gust,precipitation,precipitation_type&" + apikey

    response = requests.request("GET", url)
    return response.json()


