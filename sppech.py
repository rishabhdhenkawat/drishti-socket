from gtts import gTTS
from playsound import  playsound

language="hi"
mytext="अनजान व्यक्ति को पहचानने के लिए बोलिये जाने। "
myobj=gTTS(text=mytext,lang=language)
myobj.save("welcome11.mp3")
playsound("welcome11.mp3")