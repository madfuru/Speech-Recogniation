import os
import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
from web_auto1 import *
from web_auto2 import *
from recommentation import *
from word import *
import datetime
from Jarvis import *

security_key ='9941'
engine = p.init('sapi5')
recording = sr.Recognizer()
r1 = sr.Recognizer()
engine = p.init('sapi5')
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
    engine.setProperty('voice',voice.id)

engine.say("Hello welcome sir")
engine.runAndWait()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("say")
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print(text)
    except Exception as e:
        print(e)
#cue for giving instruction


#giving instruction


#getting info to wifi
r2 = sr.Recognizer()
engine.say('say security key')
engine.runAndWait()
with sr.Microphone() as source :
    r2.adjust_for_ambient_noise(source)
    print("say something")
    audio = r2.listen(source)
    try :
        print("k")
        instruction = r2.recognize_google(audio)
        if instruction == security_key :
            engine.say('Access granted')
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine.say('current time is' +time)
            engine.runAndWait()
            while True:
                r2 = sr.Recognizer()
                engine.say('what you want mathan')
                engine.runAndWait()
                with sr.Microphone() as source :
                    r2.adjust_for_ambient_noise(source)
                    print("say something")
                    audio = r2.listen(source)
                    try :
                        instruction = r2.recognize_google(audio)
                        print(instruction)
                    except Exception as e :
                        print(e)

                r3 = sr.Recognizer()
                if "information" in instruction :
                    engine.say("information about what madan?")
                    engine.runAndWait()
                    with sr.Microphone() as source1 :
                        r3.adjust_for_ambient_noise(source1)
                        print('say')
                        audio1 = r1.listen(source1)
                        try :
                            information = r3.recognize_google(audio1)
                            bot = info()
                            bot.get_info(information)
                            print(information)
                        except Exception as e :
                            print(e)

                r4 = sr.Recognizer()
                if "review" in instruction :
                    engine.say("What is the name of movie ? sir")
                    engine.runAndWait()
                    with sr.Microphone() as source2 :
                        r4.adjust_for_ambient_noise(source2)
                        print("tell the movie name")
                        audio3 = r4.listen(source2)
                        try :
                            review = r4.recognize_google(audio3)
                            bot = Movie()
                            bot.movie_review(review)
                        except Exception as e :
                            print(e)

                # Meaning of the word
                r5 = sr.Recognizer()
                if "meaning" in instruction :
                    engine.say("which word meaning you want? sir")
                    engine.runAndWait()
                    with sr.Microphone() as source3 :
                        r5.adjust_for_ambient_noise(source3)
                        audio4 = r5.listen(source3)
                        print("kk")
                        try :
                            print('kk')
                            meaning = r5.recognize_google(audio4)
                            mean(meaning)
                        except Exception as e :
                            print(e)

                # search in youtube
                r6 = sr.Recognizer()
                if "YouTube" in instruction :
                    engine.say("What can i search you sir.")
                    engine.runAndWait()
                    with sr.Microphone() as source4 :
                        r6.adjust_for_ambient_noise(source4)
                        print('say')
                        audio5 = r6.listen(source4)
                        try :
                            music = r6.recognize_google(audio5)
                            print('lol ')
                            bot = Music()
                            bot.play(music)
                        except Exception as e :
                            print(e)

                # about jarvis
                r7 = sr.Recognizer()
                if "what is your name" in instruction :
                    engine.say("I am sapi, Just A Rather Very Intelligent System")
                    engine.runAndWait()

                # offline music
                r8 = sr.Recognizer()
                if "offline music" in instruction :
                    engine.say("Which music you want sir")
                    engine.runAndWait()
                    with sr.Microphone() as source5 :

                        r8.adjust_for_ambient_noise(source5)
                        print('Say')
                        audio6 = r8.listen(source5)
                        try :
                            off_music = r8.recognize_google(audio6)
                            bot = offine_music()
                            bot.desktop_music(off_music)
                            engine.say('enjoy the song sir')
                            engine.runAndWait()

                        except Exception as e :
                            print(e)
                r9 = sr.Recognizer()
                if "exit" in instruction :
                    engine.say("Thank you sir ,come back again")
                    engine.runAndWait()
                    with sr.Microphone() as source5 :
                        r9.adjust_for_ambient_noise(source5)
                        print('exit')
                        break
                r10 = sr.Recognizer()
                if "shutdown" in instruction :
                    down = engine.say("do you really want to shutdowm")
                    engine.runAndWait()
                    with sr.Microphone() as source5 :
                        r10.adjust_for_ambient_noise(source5)
                        print('hmm')
                        audio6 = r10.listen(source5)
                        exit = r10.recognize_google(audio6)
                        if 'yes' == exit:
                            engine.say("ok thank you sir")
                            os.system('shutdown /s /t 1')
                        else:
                            engine.say('ok sir')
                            engine.runAndWait()
                r11 = sr.Recognizer()
                if "restart" in instruction :
                    down = engine.say("do you really want to restart")
                    engine.runAndWait()
                    with sr.Microphone() as source5:
                        r11.adjust_for_ambient_noise(source5)
                        print('kk')
                        audio6 = r10.listen(source5)
                        restart = r10.recognize_google(audio6)
                        if 'yes' == restart:
                            os.system('shutdown /r /t 1')
                        else:
                            engine.say('ok sir')
                            engine.runAndWait()
                r12 = sr.Recognizer()
                if "open Notepad" in instruction :
                    engine.say("Ok Sir")
                    engine.runAndWait()
                    bot = Music()
                    bot.notepad('')
                    engine.say("I can ready to write sir, say something")
                    engine.runAndWait()
                    with sr.Microphone() as source4:
                        r12.adjust_for_ambient_noise(source4)
                        print('say')
                        audio5 = r12.listen(source4)
                        try :
                            write = r12.recognize_google(audio5)
                            bot = Music()
                            bot.notepad(write)
                            break
                        except Exception as e :
                            print(e)

                r13 = sr.Recognizer()
                if "send mail" in instruction :
                    engine.say("say the sender mail id")
                    engine.runAndWait()
                    with sr.Microphone() as source5 :
                        r13.adjust_for_ambient_noise(source5)
                        print('Say')
                        audio6 = r13.listen(source5)
                        try :
                            to = r13.recognize_google(audio6)
                            engine.say('say the message sir')
                            engine.runAndWait()
                            r13.adjust_for_ambient_noise(source5)
                            print('Say')
                            audio7 = r13.listen(source5)
                            content = r13.recognize_google(audio7)
                            bot = Music()
                            bot.sendmail(to,content)
                            engine.say('Mail has successfully send')
                        except Exception as e :
                            engine.say('Email has no send due to some error')






        else:
            engine.say('Access Denied')
            engine.runAndWait()
    except Exception as e :
        print(e)








