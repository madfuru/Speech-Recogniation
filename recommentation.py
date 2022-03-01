import pyttsx3 as p

engine = p.init()
meaning ={
    "certification" : "the action or process of providing someone or something with an official do",
    "programming" : "the process of writing computer program",
    "skill" : "the ability to do something will,expertise",
    "automation" : "the use r introduction a human and able to replicate in a manufacturing or other processor ",
    "robot" : "A robot is a machine—especially one programmable by a computer—capable of carrying out a complex series of actions automatically."
}

translation ={
    "certification" : "Certification",
    "programming" : "Programming",
    "skill" : "Skill",
    "robot" : "robot"
}

def mean(name):
    if name in meaning:
        res = meaning[name]
        engine.say("the meaning of"+ name +"is that" + res)
        engine.runAndWait()
def translation(name):
    if name in translation:
        res = translation[name]
        engine.say("the word translate to " + res)
        engine.runAndWait()

#mean("skill")
#translation("skill")
