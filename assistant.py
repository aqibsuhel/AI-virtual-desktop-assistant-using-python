import os
import webbrowser
import json
import requests
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import pywhatkit


#setting the speaking mechanism
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
rates=engine.getProperty('rate')
# print(voices)

engine.setProperty('voice',voices[1].id)#selecting vioces by changing the value
engine.setProperty('rate',175) #rate to change the speed rate of speech

def speak(audio):#speak fun to speak
    engine.say(audio)
    engine.runAndWait()

def takecomand():#it converts voice from user to text
    r=sr.Recognizer()#having error Recoginizer=Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1#it will wait for user to catch breath for 1 second and not to implement
        audio=r.listen(source)

    try:

        print("recoginizing...")
        query=r.recognize_google(audio,language="en-in") #google recoginizing
        print(f"boss said {query}")
    except Exception as e:
        print(speak("jarvis is sorry but can you say that again."))
        return "None"
    return query

def wish():
    hour= int(datetime.now().hour)#this will give us current time in hours
    if hour<12:
        speak("ggood morning")
    elif hour>12 and hour<4:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("My name is jarvis. How may i help you boss")

def exit_jarvis():
    speak(f"i hope master that i may have been good to use to you")
    codepath = "C:\\Users\\HP\\Desktop"
    os.startfile(codepath)
    exit()

def game():
    import random
    chances = 0
    chances_left = 10
    user_score = 0
    comp_score = 0
    while chances < 10:
        game1 = ["stone", "paper", "scissor"]
        comp_choice = random.choice(game1)
        print("enter your choice:\nstone\npaper\nscissor")
        choice = input(speak("enter your choice:\nstone\npaper\nscissor"))
        if choice == comp_choice:
            print((f"computer choice is {comp_choice}\nno one wins\nuser score is={user_score + 1}:::computer score is={comp_score + 1}"))
            print(speak(f"computer choice is {comp_choice}\nno o"
                        f"ne wins\nuser score is {user_score + 1} computer score is{comp_score + 1}"))
            comp_score = comp_score + 1
            user_score = user_score + 1
            chances_left = chances_left - 1
            print((f"chances left={chances_left}"))
            print(speak(f"chances left {chances_left}"))
            chances = chances + 1
        elif comp_choice == "stone" and choice == "paper":
            print((f"computer choice is {comp_choice}\nyou win \n "
                        f"user score is={user_score + 1}:::computer score is={comp_score}"))
            print(speak(f"computer choice is {comp_choice}\nyou win \n "
                  f"user score is {user_score + 1} computer score is{comp_score + 1}"))
            user_score = user_score + 1
            chances_left = chances_left - 1
            print((f"chances left={ chances_left}"))
            print(speak(f"chances left{ chances_left}"))
            chances = chances + 1
        elif comp_choice == "stone" and choice == "scissor":
            print((f"computer choice is {comp_choice}\nyou lose \n"
                        f"user score is={user_score}:::computer score is={comp_score + 1}"))
            print(speak(f"computer choice is {comp_choice}\nyou lose \n"
                  f"user score is {user_score + 1} computer score is{comp_score + 1}"))
            comp_score = comp_score + 1
            chances_left = chances_left - 1
            print((f"chances left={ chances_left}"))
            print(speak(f"chances left { chances_left}"))
            chances = chances + 1
        elif comp_choice == "paper" and choice == "stone":
            print((f"computer choice is {comp_choice}\nyou lose \n"
                        f"user score is={user_score}:::computer score is={comp_score + 1}"))
            print(speak(f"computer choice is {comp_choice}\nyou lose \n"
                  f"user score is {user_score + 1} computer score is{comp_score + 1}"))
            comp_score = comp_score + 1
            chances_left = chances_left - 1
            print((f"chances left={ chances_left}"))
            print(speak(f"chances left { chances_left}"))
            chances = chances + 1
        elif comp_choice == "paper" and choice == "scissor":
            print((f"computer choice is {comp_choice}\nyou win \n"
                        f"user score is={user_score + 1}:::computer score is={comp_score}"))
            print(speak(f"computer choice is {comp_choice}\nyou win \n"
                  f"user score is {user_score + 1} computer score is{comp_score + 1}"))
            user_score = user_score + 1
            chances_left = chances_left - 1
            print((f"chances left={ chances_left}"))
            print(speak(f"chances left { chances_left}"))
            chances = chances + 1
        elif comp_choice == "scissor" and choice == "paper":
            print((f"computer choice is {comp_choice}\nyou lose \n"
                        f"user choice is={user_score}:::computer choice is={comp_score + 1}"))
            print(speak(f"computer choice is {comp_choice}\nyou lose \n"
                  f"user score is {user_score + 1} computer score is{comp_score + 1}"))
            comp_score = comp_score + 1
            chances_left = chances_left - 1
            print((f"chances left={chances_left}"))
            print(speak(f"chances left {chances_left}"))
            chances = chances + 1
        elif comp_choice == "scissor" and choice == "stone":
            print((f"computer choice is {comp_choice}\nyou win \n"
                        f"user score is={user_score + 1}:::computer score is={comp_score}"))
            print(speak(f"computer choice is {comp_choice}\nyou win \n"
                  f"user score is {user_score + 1} computer score is{comp_score + 1}"))
            user_score = user_score + 1
            chances_left = chances_left - 1
            print((f"chances left={ chances_left}"))
            print(speak(f"chances left {chances_left}"))
            chances = chances + 1
        elif choice=="exit":
            exit()
        else:
            print(("WRONG INPUT"))
            print(speak("WRONG INPUT"))
    if chances == 10:
        if user_score > comp_score:
            print(("GAME OVER\nUSER WINS THE GAME"))
            print(speak("GAME OVER\nUSER WINS THE GAME"))
        elif user_score < comp_score:
            print(("GAME OVER\nCOMPUTER WINS THE GAME"))
            print(speak("GAME OVER\nCOMPUTER WINS THE GAME"))
    else:
        print(("WRONG OUTPUT"))
        print(speak("WRONG OUTPUT"))

def pause():
    import time #import time here as it will create problem with date time
    print(speak("ok boss i will wait for you 10 seconds"))
    try:
        time.sleep(10)
    except Exception as e:
        print(e)

def weather():
        API_key = "bdeb1878dd4610f6fbb7a90602d11715"
        url = f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API_key}"
        data = requests.get(url)#getting url
        data_text = data.text#converting url into text
        # print(data_text)
        sort = json.loads(data_text)#js compatible file to readable mode
        sorting = sort["main"]#sorting dict to get desired item
        temperature = sorting["temp"]
        feellike=sorting["feels_like"]
        speak(f"the current temperature is {temperature} and feels like {feellike}")

def whatsapp():
    #taking no,messeag etc as parameter to pass in sendmessage()
    print("sir, kindly enter number you want to send message with country code")
    speak("sir, kindly enter number you want to send message with country code")
    number = input()
    print("sir, please enter a message that you want to send")
    speak("sir, please enter a message that you want to send")
    message=input()
    try:
        print("sir, please enter at what hour the message should be sent in 24 hour format")
        speak("sir, please enter at what hour the message should be sent in 24 hour format")
        hour=int(input())
        print("sir, please enter at what minute the message should be sent ")
        speak("sir, please enter at what minute the message should be sent ")
        minutes = int(input())
    except ValueError:
        print("sir please enter in integers not in sentence or string")
        speak("sir please enter in integers not in sentence or string")
    a=pywhatkit.sendwhatmsg(number,message,hour,minutes)
    speak(a)
    exit()

if __name__ == '__main__':
    wish()
    time=datetime.now()


    while True:
        query=takecomand().lower()
        if "wikipedia" in query:
            speak("searching your result in wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif "your name" in query:
            speak(f"my name is jarvis and i was created by  mr.Aqib qureshi on {time}")
        elif  "by" in query:
            exit_jarvis()
        elif "get lost" in query:
            exit_jarvis()
        elif "shut up" in query:
            exit_jarvis()
        elif "youtube" in query:
            webbrowser.open("youtube.com")
        elif "google" in query:
            webbrowser.open("google.com")
        elif "news" in query:
            speak("todays news is")
            #getting api request
            data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=4dc2c8953a984154bec72a4a047a9fe2")
            text_data = (data.text)#converting api into text
            sort = json.loads(text_data)#parsing text_data
            art = (sort["articles"])#taking only article
            for articles in art:
                speak(articles["title"])#reading only title of each article
                speak("moving to the next topic")
        elif "game" in query:
            speak("ok lets play stone paper and scissor")
            game()
        elif "how are you" in query:
            speak("i am fine boss as long as you are fine")
        elif "god" in query:
            speak("I would ask that you address your spiritual questions to someone more qualified to comment. Ideally human")
        elif "siri or jarvis" in query:
            speak("J.A.R.V.I.S. and siri have certain differences - J.A.R.V.I.S. is fictional while Siri is real.J.A.R.V.I.S. is way more advanced than Siri is.... "
                  "Like JARVIS can control physical objects for eg. Picking up the objects, throwing fire extinguisher, creating 3D virtual models of physical objects, tracing phone calls, encryption-decryption of information, making physics calculations etc. And as it is embedded in Iron man suit it can provide navigation, suit status etc. just by the speech recognition of Tony Stark While Siri is limited to respond to some specific voice commands and is device specific.")
        elif "time" in query:
            now=datetime.now()
            time1=(now.time())
            speak(f"sir the time is{time1}")
        elif "date" in query:
            now = datetime.now()
            date1=(now.date())
            speak(f"sir the date is {date1}")
        elif "movie" in query:
            movie_dir="C:\\Users\\HP\\Desktop\\movies"#creating directory to acess
            movies=os.listdir(movie_dir)#creating list of folders in that directory
            speak("which movie would you like to play")
            print(movies)
            movie_query=takecomand().lower()#assigining take command
            if "suicide" in movie_query:
                os.startfile(os.path.join(movie_dir,movies[0]))#startin the directory and opening movie directory and play that particular file
            elif "villanie" in movie_query:
                os.startfile(os.path.join(movie_dir,movies[2]))
            elif "venom" in movie_query:
                os.startfile(os.path.join(movie_dir,movies[1]))
        elif "pause" in query:
            pause()
        elif "message" in query:
            whatsapp()
        elif "weather today" in query:
            weather()
        elif "netflix" in query:
            webbrowser.open("https://www.netflix.com/watch/81262746?trackId=13752289")