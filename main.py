import sched, time
from getWeather import getWeather

s = sched.scheduler(time.time, time.sleep)

def start():
    response = getWeather()
    
    s.enter(120, 1, start)


s.enter(0, 1, start)
s.run()
