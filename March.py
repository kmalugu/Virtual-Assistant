import pyttsx3  #pip install pyttsx3 == text data into speech
import datetime
import speech_recognition as sr #pip install SpeechRecognition == converts voice to text
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage, Message
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
import pyjokes

engine = pyttsx3.init('sapi5')
#get voices of assistant
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id) # 0 for male voice and 1 for female voice

#speak function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#time function
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)

#greeting function
def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("March Here. How can I help you?")

#takecommand using written input
def takecommandCMD():
    query = input("Please tell me how I can I help you?\n")
    return query

def takecommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(receiver, senderemail, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak("What should I search for?")                             
    search = takecommandMic()
    wb.open('https://www.google.com/search?q='+search)


if __name__ == "__main__":
    greeting()
    while True:
        query = takecommandMic().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'hello' in query:
            speak("Hello Sir, March Here. How can I help you?")

        elif 'how are you' in query:
            speak("I am good Sir, what about you?")

        elif 'email' in query:
            email_list = {
                'Kartik':'karthikmalugu30@gmail.com'
            }
            try:
                speak("To whom you want to send the mail?")
                name = takecommandMic()
                receiver = email_list[name]
                speak("What is the subject of the mail?")
                subject = takecommandMic()
                speak("What is the message?")
                content = takecommandMic()
                sendEmail(receiver, subject, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the Email.")

        elif 'message' in query:
            user_name = {
                'Sujal' : '+91 95568 41200', 'ritul' : '+91 95181 45810'
            }
            try:
                speak("To whom you want to send the message?")
                name = takecommandMic()
                phone_no = user_name[name]
                speak("What is the message?")
                message = takecommandMic()
                sendwhatsmsg(phone_no, message)
                speak("Message has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the Message.")

        elif 'wikipedia' in query:
            speak('Searching On wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak("What should I search on YouTube?")
            topic = takecommandMic()
            pywhatkit.playonyt(topic)
            
        elif 'thank you' in query:
            speak("Welcome Sir")
            break

        elif 'good' in query:
            speak("That's great sir.")

        elif 'fine' in query:
            speak("That's great sir.")

        elif 'age' in query:
            speak("It's just 20 years sir.")

        elif 'who created you' in query:
            speak("Karthik sir created me.")

        elif 'who made you' in query:
            speak("Karthik sir made me.")

        elif 'joke' in query:
            pyjokes()

        elif 'what can you do' in query:
            speak("I can assist you to complete tasks sir.")

        elif 'offline' in query:
            speak("Ok Sir, you can call me anytime.")
            quit()