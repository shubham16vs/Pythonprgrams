import speech_recognition as sr
#Create an obj to Recognize
r = sr.Recognizer()
#import source file
with sr.AudioFile("sampleaudio.wav") as source:
 audio = r.listen(source)
 try:
 text = r.recognize_google(audio)
 print("Working on...")
 print(text)
 except:
 print("Sorry run again.")