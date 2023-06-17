import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)
engine.say("hello kesu have a good day")
engine.runAndWait()



