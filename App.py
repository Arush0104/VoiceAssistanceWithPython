import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("I am Jarvis. How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('the-email-you-want-to send-to', 'less-secure-app-password')
    server.sendmail('the-email-you-want-to send-to', to, content)
    server.quit()
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Here you are")
        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.com/")
            speak("Here you are")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Here you are")
        elif 'open w3school' in query:
            webbrowser.open("https://www.w3schools.com/")
            speak("Here you are")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("Here you are")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("Here you are")
       
        
       
        elif 'play music' in query:
            music_dir = 'music-path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(strTime)
        
        
        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "the-email-you-want-to send-to"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry, i am not able to send this email!")

        elif 'goodbye' in query:
                speak("Goodbye, have a nice day!")
                sys.exit()

        elif 'hello' in query:
            speak("Hello how are you!")

        if 'i am fine' in query:
            speak("Nice, so how may i help you?")

        elif 'i am not fine' in query:
            speak("Sorry, just be positive and everything will be well")
        elif 'who are you' in query:
            speak("i am a simple voice assistant that was created with python 3")
        
