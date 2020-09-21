import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning Pouria!")
    elif (hour <= 12 and hour < 18):
        speak("Good Afternoon Pouria!")
    else:
        speak("Good Evening Pouria!")
    speak("What Can I do for you today?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"Is this what you're saying:? {query}")
    except Exception as e:
        print(e)
        speak("I didn't get that. Say it again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # LOGICS....
        if "wikipedia" in query:
            speak("Searching in Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("Found it! According to Wikipedia")
            speak(result)
        if "good bye" in query or "bye" in query or "shut down" in query or "shutdown" in query or "see you later" in query or "go offline" in query:
            # query = query.replace("bye", "")
            phrases = ["Bye! Have fun!", "Bye My lord", "Shutting down", 
            "Going offline", "See you later", "Good bye my sir"]
            This_phrase = random.randint(0,5)
            speak(phrases[This_phrase])
            break
        if "who" in query and "are" in query and "you" in query:
            #  query = query.replace("who are you", "")
            speak("I'm an Artificial intelligence made by Pouria")
        if "who is pouria" in query:
            speak("Pouria is talented Human who loves Technology")
        if "who is he" in query:
            speak("Pouria is talented Human who loves Technology")
        if "who is your boss" in query:
            speak("My boss is Pouria")
        if "what time is it" in query:
            a = str(datetime.datetime.now().hour)
            b = str(datetime.datetime.now().minute)
            if(int(b) < 10):
                speak(f"Yes! It's {a} oh {b}")
            else:
                speak(f"Sure! It's {a} and {b}")
            

            
