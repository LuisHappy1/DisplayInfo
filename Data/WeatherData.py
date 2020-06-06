class WeatherData: 
    def __init__(self, temp=0, feelsLike=0, windSpeed=0, windGust=0, humidity=0, weatherCode='', precipitationType=''):
        self.temp = temp
        self.feelsLike = feelsLike
        self.windSpeed = windSpeed
        self.windGust = windGust
        self.humidity = humidity
        self.weatherCode = weatherCode
        self.precipitationType = precipitationType

    # Getters
    def getTemperature(self):
        return self._temp
    def getFeelsLike(self):
        return self._feelsLike
    def getWindSpeed(self): 
        return self._windSpeed
    def getWindGust(self):
        return self._windGust
    def getHumidity(self):
        return self._humidity
    def getWeatherCode(self):
        return self._weatherCode
    def getPrecipitationType(self):
        return self._precipitationType


    # Setters
    def setTemperature(self, x):
        self._temp = x
    def setFeelsLike(self, x):
        self._feelsLike = x
    def setWindSpeed(self, x):
        self._windSpeed = x
    def setWindGust(self, x):
        self._windGust = x
    def setHumidity(self, x):
        self._humidity = x
    def setWeatherCode(self, x):
        self._weatherCode = x
    def setPrecipitationType(self, x):
        self._precipitationType = x
