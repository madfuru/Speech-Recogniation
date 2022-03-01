import pyttsx3 as p

engine = p.init()
volume= engine.getProperty("voices")
print(volume)


engine.say("hello how are you doing")
engine.say("what would you like me to do madan?")
engine.runAndWait()