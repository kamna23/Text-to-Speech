# Convert text to speech using python
# install pip gTTS(Google text to speech) module
# An interface to Google Translate’s Text-to-Speech API

from gtts import gTTS   #we import this module text to speech conversion
import os

# If you want from file you can change this
file1=open('sample.txt')
text=file1.read()
# text="Hello guys , ho are you , All Fine "  #text that you want to convert

language='en'  #en for English Language
obj=gTTS(text=text,lang=language,slow=False)
# we have used slow=False because our converted video will have a high speed

obj.save("sample.mp3")

#to open the video file automatically we have to import os
os.system("sample.mp3")