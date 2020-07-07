# Import basic libraries
import pyttsx3
import datetime
import speech_recognition as sr

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# Define Function for Audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Define Function for wishMe
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")   

    speak("Hello Rukshar, I  am  Jarvis, What  Can  i  do  for  you")    
 
# Define Function for takeCommand
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold= 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n") 

    except Exception as e:
        print(e) 
        print("Say that again please...")
        return "none"
    return query    


if __name__ == "__main__":
    wishMe()  
    takeCommand()
