from gtts import gTTS
import os

def readText(text):
    tts = gTTS(text)

    tts.save('weather.mp3')
    os.system("afplay weather.mp3")
