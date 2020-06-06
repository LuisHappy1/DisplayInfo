
def buildText(weatherData):
    temperature = weatherData.getTemperature()
    humidity = weatherData.getHumidity()
    windSpeed = weatherData.getWindSpeed()
    windGust = weatherData.getWindGust()
    text = 'Hello Luis, the temperature is currently {} degrees, with the humidity at {} percent, the current wind speed is {} miles per hour with gusts up to {}'.format(temperature, humidity, windSpeed, windGust)
    return text
