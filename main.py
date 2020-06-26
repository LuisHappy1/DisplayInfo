import sched, time
from getWeather import getWeather
from BuildText import buildText
from ReadText import readText
from Data.WeatherData import WeatherData


s = sched.scheduler(time.time, time.sleep)

def start():
    weatherData = WeatherData()
    getWeather(weatherData)
    response = buildText(weatherData)
    readText(response)
    s.enter(120, 1, start)


s.enter(0, 1, start)
s.run()
