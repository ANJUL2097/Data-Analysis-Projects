import os
import smtplib
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import sys


# f = open("data.out", 'a')
# sys.stdout = f

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good Afternoon")

    else:
        speak("good evening!")
    
    speak("I am Jarvis. How may I help you")
    


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
         
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    
    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anjulbhardwaj@gmail.com', 'suhavipython123')
    server.sendmail('rishulsoni2@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    # speak("rishul is a good boy"
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('searching wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak(f"{query} is Not found on wikipedia")



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")
        
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            speak("opening amazon")
        
        elif 'open flipcart' in query:
            webbrowser.open("flipcart.com")
            speak("opening flipcart")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")


        elif 'play music' in query:
            try:
                music_dir = 'C:\\Users\\rishu\\OneDrive\\Desktop\\main project\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                speak("cant play music right now")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            # codePath = "C:\\Users\\ANSHUL RISHUL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            codePath = "C:\\Users\\rishu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("i am good . how may i help you")
            print("i am good . how may i help you")

        elif 'can you hear me' in query:
            speak("yes your voice is loud and clear")
            print("yes your voice is loud and clear")

        elif 'i love you' in query:
            speak("i only love somu")

        elif 'who are you' in query:
            speak("my name is jarivs and i am a virtual assistant. devepoled by anjul bhardwaj. i can open google youtube stackoverflow and vs code more over i can give you information about anything present on wikipedia. i can send email and can perform many other tasks. if you need anything just ask, your wish is my command")
            print("my name is jarvis and i am a virtual assistant devloped by anjul bhardwaj. i can open google youtube stackoverflow and vs code more over i can give you information about anything present on wikipedia. i can send email and can perform many other tasks. if you need anything just ask, your wish is my command")
        elif 'about you' in query:
            speak("my name is jarvis and i am a virtual assistant devloped by anjul bhardwaj. i can open google youtube stackoverflow and vs code more over i can give you information about anything present on wikipedia. i can send email and can perform many other tasks. if you need anything just ask, your wish is my command")
            print("my name is jarvis and i am a virtual assistant devloped by anjul bhardwaj. i can open google youtube stackoverflow and vs code more over i can give you information about anything present on wikipedia. i can send email and can perform many other tasks. if you need anything just ask, your wish is my command")


        elif 'diksha' in query:
            speak("Doctor diksha is a professor of university institue of computing deeksha mam is a very great teacher her best qualities are he just focus on his subject and studies of a student. his way of teaching is very convinent and understandable for students")  
            print("Doctor diksha is a professor of university institue of computing deeksha mam is a very great teacher her best qualities are he is not bothered about attendence and other activities he just focus on his subject and studies of a student. his way of teaching is very convinent and understandable for students")

        elif 'bhupendra' in query:
            speak("mr. bhupinder kumar is a professor of UCBS. bhupinder sir is very great and interactive teacher his qualities are he is not only bothered about the studies of a student but also helps stundents in their personal life. he is always suportive for his students")
            print("mr. bhupinder kumar is a professor of UCBS. bhupinder sir is very great and interactive teacher his qualities are he is not only bothered about the studies of a student but also helps stundents in their personal life.  he is always suportive for his students")

        elif 'rahul' in query:
            speak("mr. rahul chauhan is a professor of UCBS. rahul sir is a great teacher he tries to give student every important information about the subject and more over he motivates students to do better in their life")
            print("mr. rahul chauhan is a professor of UCBS. rahul sir is a great teacher he tries to give student every important information about the subject and more over he motivates students to do better in their life")

        elif 'ritu' in query:
            speak("Doctor ritu sharma  is a proffessor of UCBS. ritu ma'am is the best teacher and she has vast knowledge of her subjects and with help of real world examples she makes every topic understandable for the student")
            print("Doctor ritu sharma  is a proffessor of UCBS. ritu ma'am is the best teacher and she has vast knowledge of her subjects and with help of real world examples she makes every topic understandable for the student")

        elif 'gurmeet' in query:
            speak("gurmeet is an office staff in university intitute of computing")
            print("gurmeet is an office staff in university institute of computing")

        elif 'manisha malhotra' in query:
            speak("professor Doctor manisha malhotra is director of university institue of computing. mam has a great personality and a great experience in academics")
            print("professor Doctor manisha malhotra is director of university institue of computing. mam has a great personality and a great experience in academics")

        elif 'UIC' in query:
            speak("u i c  stands for university institue of computing")
            print("u i c  stands for university institute of computing")
        
        

        elif 'exit' in query:
            speak("ok bye have a nice day")
            print("ok bye have a nice day")
            exit()


        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "rishulsoni2@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry unable to send email at this moment")



# f.close()           
        


    
