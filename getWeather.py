from dotenv import load_dotenv
import json, requests, os
load_dotenv()

def getWeather(weatherData):
    apikey = "apikey=" + os.getenv("CLIMACELL_APIKEY")

    url = "https://api.climacell.co/v3/weather/realtime?lat=41.574&lon=-93.707&unit_system=us&fields=temp,feels_like,weather_code,humidity,wind_speed,wind_gust,precipitation,precipitation_type&" + apikey

    response = requests.request("GET", url)
    responseJson = response.json()

    weatherData.setTemperature(str(round(responseJson.get('temp').get('value'))))
    weatherData.setFeelsLike(str(round(responseJson.get('feels_like').get('value'))))
    weatherData.setWindSpeed(str(round(responseJson.get('wind_speed').get('value'))))
    weatherData.setWindGust(str(round(responseJson.get('wind_gust').get('value'))))
    weatherData.setHumidity(str(round(responseJson.get('humidity').get('value'))))
    weatherData.setWeatherCode(responseJson.get('weather_code').get('value'))
    weatherData.setPrecipitationType(responseJson.get('precipitation_type').get('value'))
