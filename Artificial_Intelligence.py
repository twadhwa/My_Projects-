import pyttsx3 as ptt
import datetime as dt
import speech_recognition as Sr


engine = ptt.init("sapi5")
# sapi5 is the voices given by microsoft

voices = engine.getProperty("voices")

"""
for i in range (len(voices)):
    print(voices[i].id )
# Used to print the details of the voice we are using
We have 2 voices in our computer 
"""


engine.setProperty("voice", voices[1].id)


def speak(audio):

    """This function will convert all the strings to audio"""
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """This function will Greet once you enter """
    hour = int(dt.datetime.now().hour)
    if hour > 0 and hour <12  :
        speak("Good Morning Sir!!!!")

    elif hour > 12 and hour < 18 :
        speak("Good Afternoon!!!!")

    else :
        speak("Good evening")

    speak("HY I am cutie's assistant, how may I help you")

def take_commond():
    """This function will take audio input from the user and will print it
    Just the opposite of the speak function """

    r = Sr.Recognizer()
    with Sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    # We use try whenever we know that an error can come
    try:
        print("Recognizing.......")
        query = r.recognize_google(audia, language= "en-in")















