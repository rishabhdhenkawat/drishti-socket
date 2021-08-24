from gtts import gTTS
from playsound import  playsound

language="hi"
mytext='''मुझे आपके सामने एक लेख मिला है'''
myobj=gTTS(text=mytext,lang=language)
myobj.save("welcome16.mp3")
playsound("welcome16.mp3")