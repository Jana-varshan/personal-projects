import pyttsx3
from random import choice
import pyaudio
import speech_recognition as sr
import web
from datetime import datetime
import openai
import smtplib
import socket

current_time = datetime.now()
current_hour = current_time.strftime('%H')
web = web.infow()

runner = pyttsx3.init()
main_loop =True
openai.api_key = "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"

# setting voice prop
k = runner.getProperty("voices")
runner.setProperty("rate", 160)
runner.setProperty("voice", k[2].id)


def speak(text1):
    print(text1)
    runner.say(text1)
    runner.runAndWait()


sal = ["dude", "buddy", "Pal", "Mate", "Friend", "Bro", "Amigo", "Chum", "Homie", "Fella", "Chap", "boss", "sir"]

while True:
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source)

        try:
            print("listing....")
            audio = r.listen(source, 5)

            text = r.recognize_google(audio)

            if "wake up" in text.lower():

                if int(current_hour) <= 10:
                    speak(f"good morning boss , setting up all the system online for you.")
                elif 12 >= int(current_hour) > 10:
                    speak("how was your day boss, dusting the systems just a minute .")
                elif 12 < int(current_hour) <= 18:
                    speak("noon buddy , 3 ")
                    speak("2")
                    speak("and")
                    speak("system's up.")
                else:
                    speak("good evening sir, grab a cup of coffee while i make things ready .")
                # main_loop = True

                while main_loop:
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source)
                        try:
                            print("listing....")
                            audio = r.listen(source)

                            text = r.recognize_google(audio)

                            if "friday" in text.lower():
                                speak("yes boss")
                                with sr.Microphone() as source:
                                    r.energy_threshold = 3000
                                    r.adjust_for_ambient_noise(source)


                                    try:
                                        print("listing....")
                                        audio = r.listen(source)

                                        text = r.recognize_google(audio)

                                        if "google" and "me" in text.lower():
                                            speak(" yes boss what do you want me too google ")
                                            with sr.Microphone() as source:
                                                r.energy_threshold = 3000
                                                r.adjust_for_ambient_noise(source)
                                                try:
                                                    print("listing....")
                                                    audio = r.listen(source)

                                                    text = r.recognize_google(audio)
                                                    web.google(query=text.lower())
                                                except sr.UnknownValueError:
                                                    pass
                                    except sr.UnknownValueError:
                                        pass
                        except sr.UnknownValueError:
                            pass
        except sr.UnknownValueError:
            pass
    # else:
    # continue

    # with sr.Microphone() as source:
    #     print("again")
    #     r.energy_threshold = 10000
    #     r.adjust_for_ambient_noise(source, 0.5)
    # audio = r.listen(source)
    # text = r.recognize_google(audio)
    # print(text)

    # if "friday" in text.lower():
    #     print("listen")
    #     if ("what" and "about" and "you") or ("about" and "how" and "you") or ("about" and "you") or ("you"):
    #         speak(f"It's all good here {choice(sal)}, what can i do")
