from gtts import gTTS
import os

def readText(text):
    tts = gTTS(text)

    tts.save('speech/weather.mp3')
    os.system("afplay speech/weather.mp3")
