import datetime
import threading
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import random
import json
import requests
import pyautogui
import time
import sys
from pynput.keyboard import Controller as key_ctrl
import pywhatkit
import PyPDF2
import sqlite3
import operator
from bs4 import BeautifulSoup
import psutil
import speedtest
from googletrans import Translator
from pywikihow import search_wikihow
import pyjokes
from tkinter import *
from tkinter import filedialog

# import win32gui, win32con
# For hiding GUI window
# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide, win32con.SW_HIDE)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


'''--------------------------------------------------------------------------------------------------------------------
--------------------------------------------Functions for executing tasks----------------------------------------------
---------------------------------------------------------------------------------------------------------------------'''


window = Tk()
window.resizable(False, False)
# global iris_says
iris_says = StringVar()

photo = PhotoImage(file="IrisLogo.png")
window.iconphoto(False, photo)

global db_phone
db_phone = False
search_box_variable = StringVar()
search_box_variable1 = StringVar()
user_says = StringVar()
iris_says.set("Start")

user_says.set(" USER")
window.update()

keyboard = key_ctrl()


def label_setter(argument1):
    if len(argument1) >= 500:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:250]}\n {argument1[250:300]}\n {argument1[300:350]}\n {argument1[350:400]}\n {argument1[400:450]}")
    elif len(argument1) >= 450:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:250]}\n {argument1[250:300]}\n {argument1[300:350]}\n {argument1[350:400]}\n {argument1[400:450]}")
    elif len(argument1) >= 400:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:250]}\n {argument1[250:300]}\n {argument1[300:350]}\n {argument1[350:400]}\n {argument1[400:len(argument1)]}")
    elif len(argument1) >= 350:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:250]}\n {argument1[250:300]}\n {argument1[300:350]}\n {argument1[350:len(argument1)]}")
    elif len(argument1) >= 300:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:250]}\n {argument1[250:300]}\n {argument1[300:len(argument1)]}")
    elif len(argument1) >= 250:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:250]}\n {argument1[250:len(argument1)]}")
    elif len(argument1) >= 200:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:200]}\n {argument1[200:len(argument1)]}")
    elif len(argument1) >= 150:
        iris_says.set(
            f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:150]}\n {argument1[150:len(argument1)]}")
    elif len(argument1) >= 100:
        iris_says.set(f"{argument1[0:50]}\n {argument1[50:100]}\n {argument1[100:len(argument1)]}")
    elif len(argument1) >= 50:
        iris_says.set(f"{argument1[0:50]}\n {argument1[50:len(argument1)]}")
    else:
        iris_says.set(f"{argument1[0:len(argument1)]}")

    window.update()


def about_me():
    iris_says.set("I am a Virtual Assistant developed by 3 upcoming \nEngineers")
    window.update()
    speak("I am a Virtual Assistant developed by 3 upcoming engineers")
    iris_says.set("Their names are: Meet, Yagnik and Vasu")
    window.update()
    speak("Their names are: Meet, Yagnik and Vaasu")
    iris_says.set("I am still in the learning phase,so please \nforgive me for any inconvenience caused")
    window.update()
    speak("I am still in the learning phase, so please forgive me for any inconvenience caused")


def getdate():
    """This function is used for getting time"""
    return datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")


def speak(audio):
    """This function enables the IRIS to speak"""
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """This function wishes the user according to time and asks for command"""
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        iris_says.set("Good Morning!")
        window.update()
        speak("Good Morning!")
    elif 12 <= hour < 14:
        iris_says.set("Good Noon!")
        window.update()
        speak("Good Noon!")
    elif 14 <= hour < 17:
        iris_says.set("Good Afternoon!")
        window.update()
        speak("Good Afternoon!")
    elif 17 <= hour < 20:
        iris_says.set("Good Evening!")
        window.update()
        speak("Good Evening!")
    else:
        iris_says.set("Good Night!")
        window.update()
        speak("Good Night!")

    iris_says.set("I am IRIS, how may I help you?")
    window.update()
    speak("I am IRIS, how may I help you?")


def take_cmd():
    """This function takes voice command from user and converts it to text"""
    try:
        """It takes input from user and converts it to String"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening...")
            iris_says.set("Listening...")
            window.update()
            r.pause_threshold = 0.7
            r.energy_threshold = 400
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=2.5)

        try:
            print("Recognizing...")
            iris_says.set("Recognizing...")
            window.update()
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            if len(query) >= 120:
                user_says.set(f"User : {query[len(query) - 100:len(query) - 50]}\n{query[len(query) - 50:len(query)]}")
                window.update()
            elif len(query) >= 60:
                user_says.set(f"User : {query[0:50]}\n{query[50:len(query)]}")
                window.update()
            else:
                user_says.set(f"{query}")
                window.update()
            f = open("UserHistory.txt", "a")
            f.write(str([str(getdate())]) + ":" + query + "\n")

        except Exception:
            print("Say that again please...")
            iris_says.set("Say that again please...")
            window.update()
            return ""
        return query.lower()

    except Exception as e:
        iris_says.set(e)
        window.update()


def take_normal():
    """It takes input from user and converts it to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        iris_says.set("Listening...")
        window.update()
        r.pause_threshold = 1.5
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        iris_says.set("Recognizing...")
        window.update()
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        if len(query) >= 120:
            user_says.set(f"User : {query[len(query) - 100:len(query) - 50]}\n{query[len(query) - 50:len(query)]}")
            window.update()
        elif len(query) >= 60:
            user_says.set(f"User : {query[0:50]}\n{query[50:len(query)]}")
            window.update()
        else:
            user_says.set(f"{query}")
            window.update()
        window.update()
        f = open("UserHistory.txt", "a")
        f.write(str([str(getdate())]) + ":" + query + "\n")

    except Exception:
        print("Say that again please...")
        iris_says.set("Say that again please...")
        window.update()
        return ""

    return query


def take_hin():
    """It takes input from user and converts it to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        iris_says.set("Listening...")
        window.update()
        r.pause_threshold = 1.0
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        iris_says.set("Recognizing...")
        window.update()
        query = r.recognize_google(audio, language='hi')
        print(f"User said: {query}")
        if len(query) >= 120:
            user_says.set(f"User : {query[len(query) - 100:len(query) - 50]}\n{query[len(query) - 50:len(query)]}")
            window.update()
        elif len(query) >= 60:
            user_says.set(f"User : {query[0:50]}\n{query[50:len(query)]}")
            window.update()
        else:
            user_says.set(f"{query}")
            window.update()
        window.update()

    except:
        print("Say that again please...")
        iris_says.set("Say that again please")
        window.update()
        return ""

    return query


def take_guj():
    """It takes input from user and converts it to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        iris_says.set("Listening...")
        window.update()
        r.pause_threshold = 0.7
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        iris_says.set("Recognizing...")
        window.update()
        query = r.recognize_google(audio, language='gu-in')
        print(f"User said: {query}")
        if len(query) >= 120:
            user_says.set(f"User : {query[len(query) - 100:len(query) - 50]}\n{query[len(query) - 50:len(query)]}")
            window.update()
        elif len(query) >= 60:
            user_says.set(f"User : {query[0:50]}\n{query[50:len(query)]}")
            window.update()
        else:
            user_says.set(f"{query}")
            window.update()
        window.update()

    except:
        print("Say that again please...")
        iris_says.set("Say that again please")
        window.update()
        return ""

    return query


def translate_hin():
    """It translates hindi sentences to English"""
    iris_says.set("Tell me the Line")
    window.update()
    speak("Tell me the line")
    line = take_hin()
    translate_this = Translator()
    result_hin = translate_this.translate(line)
    text_hin = result_hin.text
    label_setter(f"The translation is {text_hin}")
    window.update()
    speak(f"The translation is {text_hin}")


def translate_guj():
    """It translates gujarati sentences to English"""
    iris_says.set("Tell me the Line")
    window.update()
    speak("Tell me the line")
    line = take_guj()
    translate_this = Translator()
    result_guj = translate_this.translate(line)
    text_hin = result_guj.text
    label_setter(f"The translation is {text_hin}")
    window.update()
    speak(f"The translation is {text_hin}")


def iris_starter():
    """Checks if user has selected a language and starts IRIS in that language accordingly"""
    try:
        file5 = open('language.txt', 'r+')
        iris_says.set("Input language for your assistant")
        window.update()
        speak("Input language for your assistant")
        ch4 = take_cmd()
        file5.write(ch4)
        file5.close()
        file6 = open('language.txt', 'r+')
        ch5 = file6.readline()
        file6.close()
        if 'english' in ch5:
            assistant_in_english()
        elif 'hindi' in ch5:
            assistant_in_hindi()
        elif 'gujarati' in ch5:
            assistant_in_gujarati()

    except Exception as e5:
        print(e5)


def select_phone_number_name(searched_phone_number):
    """
    This function selects name of user to send message from its argument searched_phone_number
    and checks if user is available in database
    :param searched_phone_number:
    :return:
    """

    cursor2 = conn2.cursor()
    cursor2.execute("SELECT * FROM phonenumber WHERE name=? ", (searched_phone_number,))
    rows = cursor2.fetchall()
    try:
        for row in rows:
            required_number_name = row[0]
            return required_number_name
    except:
        label_setter(f"No contact for username {searched_phone_number} found")


def select_phone_number(searched_phone_number):
    """
    This function selects phone number from its argument searched_phone_number, which is name of user to send message
    :param searched_phone_number:
    :return:
    """
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT * FROM phonenumber WHERE name=? ", (searched_phone_number,))
    rows = cursor2.fetchall()

    try:
        for row in rows:
            required_number = row[1]
            return required_number

    except:
        label_setter(f"No contact for user {searched_phone_number} found")


def create_and_update_phone_number_database(val1, val2):
    """
     This function creates PhoneNumber database table if not exist
     or if PhoneNumber table exists it inserts data from user choice
     :return:
     """
    try:
        global db_phone
        # conn2 = sqlite3.connect('PhoneNumber.db')
        cursor2 = conn2.cursor()
        cursor2.execute("CREATE TABLE IF NOT EXISTS phonenumber(name char(30) primary key,phonenumber char(13));")
        s1_name = val1
        s1_number = val2
        cursor2.execute("""
        INSERT INTO phonenumber(name,phonenumber)
        VALUES (?,?)
        """, (s1_name, s1_number))

        conn2.commit()
        db_phone = True

    except:
        db_phone = False
        iris_says.set("User name already exists")
        window.update()
        speak("User name already exists")


def display_all_number():
    """Displays all phone numbers/ For development use"""
    cursor = conn2.cursor()
    cursor.execute("SELECT * FROM phonenumber")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def operators(op):
    """Selects operator for vocal calculator"""
    return {
        ('+' or 'plus'): operator.add,
        ('-' or 'minus'): operator.sub,
        'x': operator.mul,
        '/': operator.truediv,
    }[op]


def evaluate_expression(op1, opr, op2):
    """Evaluates expression given by user"""
    op1, op2 = int(op1), int(op2)
    return operators(opr)(op1, op2)


def search_on_google():
    """Perform search operation through Google search engine
    If user search query begins with "how" it will search on WikiHow"""
    try:
        iris_says.set("Sir what should I search on google")
        window.update()
        speak("Sir what should I search on google")
        search = take_normal()

        if 'how to ' in search:
            try:
                max_result = 1
                how_to_func = search_wikihow(query=search, max_results=max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                iris_says.set("")
                window.update()
                speak(how_to_func[0].summary)
            except:
                pywhatkit.search(search)

        else:
            try:
                search = wikipedia.summary(search, 2)
                print(search)
                label_setter(search)
                window.update()
                speak(f": According to Google : {search}")
            except:
                pywhatkit.search(search)
    except:
        iris_says.set("Some error occurred")
        window.update()
        speak("Some error occurred")


def open_notepad():
    """Opens Notepad"""
    path = "C:\\Windows\\Notepad.exe"
    os.startfile(path)


def play_music():
    """Plays random music(.mp3) from directory given by user"""
    try:
        iris_says.set("Enter directory from which you want to play \nRandom song")
        window.update()
        speak("Enter directory from which you want to play random song")
        music_dir = filedialog.askdirectory()

        def get_mp3():
            for root, dirs, files in os.walk(music_dir):
                for file in files:
                    songs = os.listdir(music_dir)
                    rand = random.choice(songs)
                    if rand.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, rand))
                        break
                    else:
                        get_mp3()
                        break
        get_mp3()

    except Exception as e4:
        print(e4)


def speak_news():
    """Fetches the latest national news and displays/provides it to User"""
    try:
        iris_says.set("News for today...Let's Begin")
        window.update()
        speak("News for today...Let's Begin")
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=70d295416b8f40969b971d8bda89d60c"
        res = requests.get(url)
        page = res.json()
        article = page['articles']
        results = []
        for ar in article:
            results.append(ar['title'])
            # print(len(ar['title']))
            label_setter(ar['title'].lower())
            window.update()
            speak(ar['title'])
            if len(results) == 5:
                break
            iris_says.set("Moving on to the next news")
            window.update()
            speak("Moving on to the next news")
        iris_says.set("That's it for today. Thanks for listening the news")
        window.update()
        speak("That's it for today. Thanks for listening the news")
    except:
        iris_says.set("Can't fetch news now")
        window.update()
        speak("Can't fetch news now")


def current_time():
    """Provides current time to User"""
    curr_time = datetime.datetime.now().strftime("%H:%M:%S")
    iris_says.set(f"The current time is {curr_time}")
    window.update()
    speak(f"The current time is {curr_time}")


def switch_win():
    """Used to switch windows"""
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")


def start_cmd():
    """Used to start command prompt"""
    os.system("start cmd")


def whatsapp_message():
    """Used to send whatsapp message"""
    try:
        iris_says.set("What should I say?")
        window.update()
        speak("What should I say?")
        message = take_normal()
        iris_says.set("Whom do you want to send message?")
        window.update()
        speak("Whom do you want to send message?")
        name2 = take_cmd()
        receiver_number = select_phone_number(name2)
        receiver_name = select_phone_number_name(name2)
        if name2 in receiver_name:
            pywhatkit.sendwhatmsg_instantly(receiver_number, message)
            time.sleep(10)
            pyautogui.press('enter')
        else:
            iris_says.set("The person is not in your contact list")
            window.update()
            speak("The person is not in your contact list")
    except:
        label_setter("Please speak valid name and try again")
        window.update()
        speak("Please speak valid name and try again")


def play_on_yt():
    """Used to play videos on YouTube"""
    try:
        iris_says.set("Please tell me the title of video")
        window.update()
        speak("Please tell me the title of video")
        video_name = take_normal()
        iris_says.set("Starting YouTube...")
        window.update()
        speak("Starting YouTube...")
        pywhatkit.playonyt(video_name)
        time.sleep(20)

    except:
        iris_says.set("Can't play video now, please try again")
        window.update()
        speak("Can't play video now, please try again")


def one_random_joke():
    """Tells one random joke"""
    joke = pyjokes.get_joke(language="en", category="all")
    label_setter(joke)
    window.update()
    speak(joke)


def inspire_me():
    """Provides a motivational quote to the user"""
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "\"" + json_data[0]['q'] + "\"" + " - " + json_data[0]['a']
    label_setter(quote)
    window.update()
    speak(quote)


def location_finder():
    """Finds location of user through IP"""
    iris_says.set("Please wait sir, let me check")
    window.update()
    speak("Please wait sir, let me check")
    try:
        ip = requests.get("https://api.ipify.org").text
        request_url = 'https://geolocation-db.com/jsonp/' + ip
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)
        country = result['country_name']
        city = result['city']
        state = result['state']
        iris_says.set(f"sir we are in {city} city,{state} state and \n{country} country")
        window.update()
        speak(f"sir we are in {city} city, {state} state and {country} country")
    except:
        label_setter("Sorry sir due to network issue I am not able to find where we are")
        window.update()
        speak("Sorry sir due to network issue I am not able to find where we are")


def screenshot():
    """Takes Screenshot of current screen, and saves it in IRIS's directory"""
    iris_says.set("Please tell me name for this screenshot")
    window.update()
    speak("Please tell me name for this screenshot")
    name = take_cmd().lower()
    iris_says.set("Sir please hold screen for few second\n I am taking screenshot")
    window.update()
    speak("Sir please hold screen for few second I am taking screenshot")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.jpg")
    iris_says.set("Your screenshot has been captured and saved")
    window.update()
    speak("Your screenshot has been captured and saved")


def pdf_reader():
    """Used to read pdf without images"""
    try:
        iris_says.set("Sir please input correct path of pdf")
        window.update()
        speak("Sir please select correct path of pdf")
        bk_name = filedialog.askopenfilename()
        book = open(bk_name, 'rb')
        reader = PyPDF2.PdfFileReader(book)
        pages = reader.numPages
        iris_says.set(f"Total number of pages in the book is {pages}")
        window.update()
        speak(f"Total number of pages in the book is {pages}")
        iris_says.set("Sir input the page number I have to read")
        window.update()
        speak("Sir input the page number I have to read")
        pg = int(take_cmd())
        page = reader.getPage(pg)
        text_pdf = page.extractText()
        label_setter(f"Reading {bk_name}".lower())
        speak(text_pdf)

    except Exception as e1:
        print(e1)
        iris_says.set("Can't read the PDF now")
        window.update()
        speak("Can't read the PDF now")


def vocal_calculator():
    """Used to calculate addition, subtraction, multiplication and division vocally"""
    try:
        iris_says.set("What should I calculate, Example 4 plus 5")
        window.update()
        speak("What should I calculate, Example 4 plus 5")
        cal = take_normal()
        iris_says.set(evaluate_expression(*(cal.split())))
        window.update()
        speak("Your result is")
        speak(evaluate_expression(*(cal.split())))
    except Exception as e3:
        print(e3)
        iris_says.set("Could not perform calculation now, please try again")
        window.update()
        speak("Could not perform calculation now, please try again")


def temperature():
    """Provides weather of user's desired city"""
    iris_says.set("speak the name of city or location")
    window.update()
    speak("speak the name of city or location")
    search = "temperature in "
    search2 = search + take_cmd()
    url = f"https://www.google.com/search?q={search2}"
    temp_req = requests.get(url)
    data = BeautifulSoup(temp_req.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    label_setter(f"current {search2} is {temp}")
    window.update()
    speak(f"current {search2} is {temp}")


def current_battery():
    """Finds current battery percentage and recommends appropriate action based on it"""
    battery = psutil.sensors_battery()
    percentage = battery.percent
    iris_says.set(f"Sir your system has {percentage} percent battery left")
    window.update()
    speak(f"Sir your system has {percentage} percent battery left")
    if percentage >= 40:
        iris_says.set("sir we have enough power to continue our work")
        window.update()
        speak("sir we have enough power to continue our work")
    elif 40 > percentage >= 20:
        iris_says.set("sir we should connect our system to charging point")
        window.update()
        speak("sir we should connect our system to charging point")
    elif percentage < 20:
        iris_says.set("sir we should immediately connect our system to charging point")
        window.update()
        speak("sir we should immediately connect our system to charging point")


def internet_speed():
    """Finds user's Network Speed and Ping"""
    iris_says.set("Please wait sir while I check your Internet Speed")
    window.update()
    speak("Please wait sir while I check your Internet Speed")
    speed_test = speedtest.Speedtest()
    download_sp = speed_test.download()
    upload_sp = speed_test.upload()
    speed_test.get_servers([])
    ping = speed_test.results.ping
    ds = float(download_sp / 800000)
    us = float(upload_sp / 800000)
    label_setter(f"Your download speed is {ds:.2f} Mbps and upload speed is {us:.2f} Mbps".lower())
    window.update()
    speak(f"Your download speed is {ds:.2f} Mbps and upload speed is {us:.2f} Mbps")
    label_setter(f"Your ping is {ping} ms".lower())
    window.update()
    speak(f"Your ping is {ping} ms")


def hello():
    """Say's Hello"""
    hi_response = ["hey", "hello", "hi", "namaste"]
    hi_resp = random.choice(hi_response)
    iris_says.set(hi_resp)
    window.update()
    speak(hi_resp)


def how_are_you():
    """Adding interactions to IRIS"""
    hay_response = ["I'm fine", "I'm good", "I'm well", "I'm OK"]
    hay_resp = random.choice(hay_response)
    iris_says.set(hay_resp)
    window.update()
    speak(hay_resp)
    iris_says.set("by the way how are you?")
    window.update()
    speak("by the way how are you? ")
    hay_usr_resp = take_cmd()
    if 'i am fine' in hay_usr_resp or 'i am good' in hay_usr_resp or 'Ok' in hay_usr_resp:
        iris_says.set("I am glad to hear that sir, how may I help you?")
        window.update()
        speak("I am glad to hear that sir, how may I help you?")
    elif 'depressed' in hay_usr_resp or 'sad' in hay_usr_resp or 'not fine' in hay_usr_resp:
        iris_says.set("Sorry to hear that, Just be calm and happy")
        window.update()
        speak("Sorry to hear that, Just be calm and happy")
        iris_says.set("Let me tell you a joke")
        window.update()
        speak("Let me tell you a joke")
        random_joke = ["What do you call a cow who plays guitar?.....A moo-sician",
                       "Know any good jokes about sodium?........NA!",
                       "Did you hear about the Minecraft movie?......It's really blockbuster",
                       "Why was 9 scared of 7?......Because 7 ate 9!",
                       "Why shouldn't you write with a broken pen?.....Because it's completely pointless"]
        ran_joke = random.choice(random_joke)
        label_setter(ran_joke)
        window.update()
        speak(ran_joke)


def sleep():
    """Puts IRIS in sleep mode, however it does not close program"""
    iris_says.set("Thanks for using IRIS, have a good day sir!")
    window.update()
    speak("Thanks for using IRIS, have a good day sir!")
    sys.exit(0)


def remember_that():
    """Remembers the information said to remember by user"""
    iris_says.set("Sir what should I remember")
    window.update()
    speak("Sir what should I remember")
    remember_msg = take_normal()
    label_setter(f"You Told Me To Remind You That: {remember_msg}")
    window.update()
    speak("You Told Me To Remind You That: " + remember_msg)
    remember = open('remember.txt', 'a')
    remember.write(remember_msg + "\n")
    remember.close()


def what_i_told_to_remember():
    """Answer's what the user told it to remember"""
    remember = open('remember.txt', 'r')
    lines = remember.readlines()
    for line in lines:
        label_setter(f"sir you told me that: {line}")
        window.update()
        speak("sir you told me that" + line)


def forget_what_i_told_to_remember():
    """Forgets what user told it to remember"""
    remember = open('remember.txt', 'r')
    d = remember.read()
    remember.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    remember = open('remember.txt', 'w+')
    for i in range(len(s)):
        remember.write(s[i])
    remember.close()
    label_setter("Removed from the list")
    speak("Removed from the list")


def notepad():
    """Converts user's speech to text, and saves it in a task file"""
    os.makedirs("C:\\Notepad\\NotepadDB", exist_ok=True)
    iris_says.set("Sir I am ready to write")
    window.update()
    speak("Sir I am ready to write")
    iris_says.set("Please tell me what I should write")
    window.update()
    speak("Please tell me what I should write")
    time_now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    filename = str(time_now).replace(":", "-") + " note.txt"
    while True:
        write = take_normal()
        if 'comma' in write or 'coma' in write:
            with open(filename, 'a') as file:
                file.write(write.replace(" comma" or ' coma' or 'comma ' or 'coma ' or 'comma' or 'coma', ", "))

        elif 'full stop' in write:
            with open(filename, 'a') as file:
                file.write(write.replace(" full stop" or 'fullstop' 'full stop' or 'full stop ', ". "))

        elif 'enter key' in write:
            with open(filename, 'a') as file:
                file.write(write.replace("enter key", " ") + "\n")

        elif write == "save file":
            with open(filename, 'a') as file:
                file.write(write.replace("save file", " "))
                break

        else:
            with open(filename, 'a') as file:
                file.write(write + " ")

    path1 = str(filename)
    path2 = "C:\\Notepad\\NotepadDB\\" + str(filename)
    os.rename(path1, path2)
    os.startfile(path2)


def realtime_notepad():
    """Writes in notepad what user said, in real time"""
    path = "C:\\Windows\\Notepad.exe"
    fileLang = open('language.txt', 'r+')
    lang = fileLang.readline()
    fileLang.close()
    if 'english' in lang:
        language = "english"
    elif 'hindi' in lang:
        language = "hindi"
    elif 'gujarati' in lang:
        language = "gujarati"

    iris_says.set("Sir I am ready to write")
    window.update()
    speak("Sir I am ready to write")
    iris_says.set("Please tell me what I should write")
    window.update()
    speak("Please tell me what I should write")
    os.startfile(path)
    time.sleep(0.25)

    while True:
        if language.__eq__("english"):
            write = take_normal()
        elif language.__eq__("hindi"):
            write = take_hin()
        elif language.__eq__("gujarati"):
            write = take_guj()

        label_setter("Typing...")
        if write == "save file" or write == "सेव फाइल":
            iris_says.set("Please check the path in window")
            window.update()
            speak("Please check the path in window")
            pyautogui.hotkey('ctrlleft', 's')
            time.sleep(2.5)
            iris_says.set("Speak the name of file: ")
            window.update()
            speak("Speak the name of file: ")
            name = take_cmd()
            if name == '':
                time_now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                filename = str(time_now).replace(":", "-") + " note.txt"
                pyautogui.typewrite(filename)
                pyautogui.press('enter')
            else:
                pyautogui.typewrite(name)
                pyautogui.press('enter')
            iris_says.set("Your file has been saved!")
            window.update()
            speak("Your file has been saved")
            break

        else:
            for iteration in write:
                keyboard.type(iteration)
                time.sleep(0.025)
            pyautogui.press('space')


def rps_game():
    """Voice command game for IRIS"""
    iris_says.set("Welcome to Rock, Paper, Scissor game")
    window.update()
    speak("Welcome to Rock, Paper, Scissor game")
    label_setter("There are 5 rounds and the One to win it most times would win")
    window.update()
    speak("There are 5 rounds and the one to win it most times would win")
    iris_says.set("So let's start")
    window.update()
    speak("So let's start")
    i = 0
    cnt_user = 0
    cnt_iris = 0
    tied = 0
    while i < 5:
        speak("your turn")
        user_choice = take_cmd()
        if 'rock' in user_choice or 'paper' in user_choice or 'scissors' in user_choice:
            moves = ['rock', 'paper', 'scissors']
            iris_choice = random.choice(moves)
            label_setter(f"IRIS: {iris_choice}")
            window.update()
            if user_choice.__eq__(iris_choice):
                iris_says.set("Its a Tie!")
                window.update()
                speak("Its a Tie!")
                tied = tied + 1
            elif user_choice.__eq__("rock") and iris_choice.__eq__("scissors") or \
                    user_choice.__eq__("paper") and iris_choice.__eq__("scissors") or user_choice.__eq__("scissors") \
                    and iris_choice.__eq__("paper"):
                iris_says.set("You Won!")
                window.update()
                speak("You Won!")
                cnt_user += 1
            else:
                iris_says.set("IRIS Won!")
                window.update()
                speak("IRIS Won!")
                cnt_iris += 1
            i += 1

        else:
            label_setter("Please speak only one from rock, paper or scissors")
            window.update()
            speak("Please speak only one from rock, paper or scissors")

    if cnt_user > cnt_iris:
        iris_says.set("You won the match!")
        window.update()
        speak("You won the match!")
    elif cnt_user == cnt_iris:
        iris_says.set("Match is tied!")
        window.update()
        speak("Match is tied!")
    else:
        iris_says.set("IRIS won the match!")
        window.update()
        speak("IRIS won the match!")


def assistant_in_english():
    """Starts IRIS in english"""
    wish_me()
    
    while True:
        query = take_cmd()
        # Logic for executing tasks based on user query

        if 'search on google' in query:
            search_on_google()

        elif 'open notepad' in query:
            open_notepad()

        elif 'play music' in query:
            play_music()

        elif 'news' in query:
            speak_news()

        elif 'current time' in query or 'time' in query:
            current_time()

        elif 'switch window' in query:
            switch_win()

        elif 'open command prompt' in query:
            start_cmd()

        elif 'send whatsapp message' in query or 'send a whatsapp message' in query:
            whatsapp_message()

        elif 'play video on youtube' in query or 'play on youtube' in query:
            play_on_yt()

        elif 'tell me a joke' in query:
            one_random_joke()

        elif 'inspire me' in query:
            inspire_me()

        elif 'where am i' in query or 'show my location' in query:
            location_finder()

        elif 'take screenshot' in query:
            screenshot()

        elif 'read the book' in query or 'read pdf' in query:
            pdf_reader()

        elif 'calculate this' in query or 'do some calculations' in query:
            vocal_calculator()

        elif 'temperature' in query or 'weather' in query:
            temperature()

        elif 'power' in query or 'battery' in query:
            current_battery()

        elif 'internet speed' in query or 'network speed' in query:
            internet_speed()

        elif 'hello' in query or 'hi ' in query:
            hello()

        elif 'translate from hindi' in query:
            translate_hin()

        elif 'remember that' in query:
            remember_that()

        elif 'what did i told you to remember' in query:
            what_i_told_to_remember()

        elif 'forget what i told you to remember' in query:
            forget_what_i_told_to_remember()

        elif 'how are you' in query or 'how you doin' in query:
            how_are_you()

        elif 'write article' in query:
            notepad()

        elif 'speak and type' in query:
            realtime_notepad()

        elif 'play a game' in query:
            rps_game()

        elif 'about you' in query or 'made you' in query or 'introduce yourself' in query:
            about_me()

        elif 'change language' in query:
            iris_starter()

        elif 'sleep' in query:
            sleep()


def assistant_in_hindi():
    """Starts IRIS in hindi"""
    wish_me()
    
    while True:
        query = take_hin()

        # Logic for executing tasks based on user query
        if 'गूगल पर खोजिए' in query:
            search_on_google()

        elif 'नोटपैड खोलिए' in query:
            open_notepad()

        elif 'गाना बजाए' in query:
            play_music()

        elif 'न्यूज' in query:
            speak_news()

        elif 'टाइम बताए' in query or 'टाइम' in query:
            current_time()

        elif 'विंडो बदलिए' in query:
            switch_win()

        elif 'कमांड प्रॉम्प्ट खोलिए' in query:
            start_cmd()

        elif 'व्हाट्सएप मैसेज भेजिए' in query:
            whatsapp_message()

        elif 'यूट्यूब पर वीडियो चलाए' in query:
            play_on_yt()

        elif 'चुटकुला सुनाइए' in query:
            one_random_joke()

        elif 'प्रेरित करे' in query:
            inspire_me()

        elif 'में कहां हूं' in query or 'मेरी लोकेशन बताए' in query:
            location_finder()

        elif 'स्क्रीनशॉट खींचिए' in query:
            screenshot()

        elif 'किताब पढ़कर सुनाएं' in query:
            pdf_reader()

        elif 'गिनती कीजिए' in query or 'कैलकुलेट कीजिए' in query:
            vocal_calculator()

        elif 'तापमान' in query or 'हवामान' in query:
            temperature()

        elif 'बैटरी' in query or 'पावर' in query or 'चार्जिंग' in query:
            current_battery()

        elif 'इंटरनेट स्पीड' in query or 'नेटवर्क स्पीड' in query:
            internet_speed()

        elif 'हाई' in query or 'नमस्ते' in query:
            hello()

        elif 'ट्रांसलेट टू इंग्लिश' in query or 'इंग्लिश में अनुवाद करें' in query:
            translate_hin()

        elif 'याद रखो' in query:
            remember_that()

        elif 'मैने आप को क्या याद रखने को कहा था' in query or 'मैने तुम्हे क्या याद रखने को कहा था' in query:
            what_i_told_to_remember()

        elif 'भुल जाओ' in query:
            forget_what_i_told_to_remember()

        elif 'आप कैसे है' in query:
            how_are_you()

        elif 'नोटपैड में लिखिए' in query:
            notepad()

        elif 'आप के बारे में बताए' in query:
            about_me()

        elif 'स्पीक एंड टाइप' in query:
            realtime_notepad()

        elif 'भाषा बदलिए' in query:
            iris_starter()

        elif 'आराम' in query or 'विश्राम' in query:
            sleep()


def assistant_in_gujarati():
    """Starts IRIS in hindi"""
    wish_me()
    
    while True:
        query = take_guj()
        # Logic for executing tasks based on user query

        if 'ગૂગલ કરો' in query or 'google કરો' in query:
            search_on_google()

        elif 'નોટપેડ ખોલો' in query:
            open_notepad()

        elif 'ગાવાનું વગાડો' in query or 'ગીત વગાડો' in query:
            play_music()

        elif 'સમાચાર' in query:
            speak_news()

        elif 'સમય' in query:
            current_time()

        elif 'વિન્ડો બદલો' in query:
            switch_win()

        elif 'કમાન્ડ પ્રોમ્પ્ટ ખોલો' in query or 'કમાંડ પ્રોમ્પ્ટ ખોલો' in query:
            start_cmd()

        elif 'મેસેજ મોકલો' in query:
            whatsapp_message()

        elif 'યુટયુબ ખોલો' in query or 'youtube ખોલો' in query:
            play_on_yt()

        elif 'જોક્સ સંભળાવો' in query:
            one_random_joke()

        elif 'સુવાક્ય સંભળાવો' in query:
            inspire_me()

        elif 'લોકેશન બતાવો' in query:
            location_finder()

        elif 'સ્ક્રીનશોટ લેજો' in query:
            screenshot()

        elif 'પીડીએફ વાંચો' in query or 'પુસ્તક વાંચો' in query:
            pdf_reader()

        elif 'ગણતરી કરો' in query:
            vocal_calculator()

        elif 'હવામાન બતાવો' in query:
            temperature()

        elif 'ચાર્જિંગ જણાવો' in query:
            current_battery()

        elif 'ઇન્ટરનેટ સ્પીડ' in query:
            internet_speed()

        elif 'હાઈ' in query or 'હેલ્લો' in query:
            hello()

        elif 'ઇંગલિશ માં અનુવાદ કરો' in query:
            translate_guj()

        elif 'યાદ રાખો' in query:
            remember_that()

        elif 'મેં તને શું યાદ રાખવા કીધેલું' in query:
            what_i_told_to_remember()

        elif 'ભૂલી જાવ' in query:
            forget_what_i_told_to_remember()

        elif 'તમે કેમ છો' in query:
            how_are_you()

        elif 'આર્ટીકલ લખો' in query:
            notepad()

        elif 'તમારા વિશે જણાવો' in query:
            about_me()

        elif 'speak and type' in query or 'સ્પીક એન્ડ ટાઈપ' in query:
            realtime_notepad()

        elif 'ભાષા બદલો' in query:
            iris_starter()

        elif 'સુઈ જાવ' in query or 'આરામ કરો' in query:
            sleep()


def full_start():
    """Initiates IRIS and starts the program"""
    try:
        file7 = open('language.txt', 'r+')
        file7.close()
        file1 = open('language.txt', 'r+')
        ch = file1.read()
        if ch == "":
            speak("Input language for your assistant")
            choice = take_cmd()
            file1.write(choice)
            file1.close()
            file3 = open('language.txt', 'r+')
            ch3 = file3.readline()
            file3.close()
            if 'english' in ch3:
                assistant_in_english()
            elif 'hindi' in ch3:
                assistant_in_hindi()
            elif 'gujarati' in ch3:
                assistant_in_gujarati()

        else:
            file2 = open('language.txt', 'r+')
            ch2 = file2.readline()
            if 'english' in ch2 or 'English' in ch2:
                assistant_in_english()
            elif 'hindi' in ch2 or 'Hindi' in ch2:
                assistant_in_hindi()
            elif 'gujarati' in ch2 or 'Gujarati' in ch2:
                assistant_in_gujarati()
            else:
                choice = "english"
                file4 = open('language.txt', 'r+')
                file4.write(choice)
                file4.close()

    except Exception as e:
        iris_says.set(e)
        window.update()


def destroy_window():
    """Closes the program"""
    window.destroy()
    engine.stop()
    sys.exit()


def update_suggestion_arg(suggest):
    """Used to search and suggest commands to user"""
    if 'google' in suggest or 'sear' in suggest:
        suggestion_variable = "Search on Google "
        return suggestion_variable
    elif 'notepad' in suggest or 'open n' in suggest:
        suggestion_variable = "Open Notepad"
        return suggestion_variable
    elif 'music' in suggest or 'mus' in suggest:
        suggestion_variable = "Play Music"
        return suggestion_variable
    elif 'news' in suggest or 'latest' in suggest or 'new' in suggest:
        suggestion_variable = "news"
        return suggestion_variable
    elif 'time' in suggest or 'current' in suggest or 'clock' in suggest:
        suggestion_variable = "Current Time or Time"
        return suggestion_variable
    elif 'window' in suggest or 'switch' in suggest:
        suggestion_variable = "Switch Window"
        return suggestion_variable
    elif 'prompt' in suggest or 'com' in suggest:
        suggestion_variable = "Open command prompt"
        return suggestion_variable
    elif 'whatsapp' in suggest or 'message' in suggest or 'whats' in suggest or 'msg' in suggest:
        suggestion_variable = "Send whatsapp message"
        return suggestion_variable
    elif 'video' in suggest or 'youtube' in suggest or 'yt' in suggest:
        suggestion_variable = "Play video on youtube"
        return suggestion_variable
    elif 'joke' in suggest or 'tell me' in suggest or 'laugh' in suggest:
        suggestion_variable = "Tell me a Joke"
        return suggestion_variable
    elif 'inspire' in suggest or 'quote' in suggest:
        suggestion_variable = "Inspire Me"
        return suggestion_variable
    elif 'location' in suggest or 'loc' in suggest or 'where' in suggest:
        suggestion_variable = "Show my location"
        return suggestion_variable
    elif 'screenshot' in suggest or 'take' in suggest or 'screen' in suggest:
        suggestion_variable = "Take Screenshot"
        return suggestion_variable
    elif 'pdf' in suggest or 'book' in suggest or 'read' in suggest:
        suggestion_variable = "Read PDF"
        return suggestion_variable
    elif 'calculator' in suggest or 'vocal' in suggest or 'calc' in suggest:
        suggestion_variable = "Calculate this"
        return suggestion_variable
    elif 'temperature' in suggest or 'weather' in suggest or 'temp' in suggest:
        suggestion_variable = "Temperature"
        return suggestion_variable
    elif 'pow' in suggest or 'charging' in suggest or 'bat' in suggest:
        suggestion_variable = "Battery or Power"
        return suggestion_variable
    elif 'network' in suggest or 'inter' in suggest or 'spee' in suggest or 'net' in suggest:
        suggestion_variable = "Internet Speed "
        return suggestion_variable
    elif 'translate' in suggest or 'hindi' in suggest or 'trans' in suggest:
        suggestion_variable = "Translate from hindi"
        return suggestion_variable
    elif 'remember' in suggest or 'rem' in suggest:
        suggestion_variable = "Remember that"
        return suggestion_variable
    elif 'told' in suggest or 'what did' in suggest:
        suggestion_variable = "What did I told you to remember"
        return suggestion_variable
    elif 'forget' in suggest:
        suggestion_variable = "Forget what I told you to remember"
        return suggestion_variable
    elif 'write' in suggest or 'article' in suggest or 'wri' in suggest:
        suggestion_variable = "Write Article"
        return suggestion_variable
    elif 'game' in suggest or 'play' in suggest:
        suggestion_variable = "Play a Game"
        return suggestion_variable
    elif 'about' in suggest or 'describe' in suggest or 'abo' in suggest:
        suggestion_variable = "About you"
        return suggestion_variable
    elif 'language' in suggest or 'change' in suggest or 'lan' in suggest:
        suggestion_variable = "Change language"
        return suggestion_variable
    elif 'sleep' in suggest or 'exit' in suggest or 'stop' in suggest or 'sl' in suggest:
        suggestion_variable = "Exit Application"
        return suggestion_variable
    elif 'speech' in suggest or 'real time' in suggest or ' to text' in suggest or 'type' in suggest or 'speak' in suggest:
        suggestion_variable = "Speak and Type"
        return suggestion_variable
    else:
        suggestion_variable = "Please Enter a\n Valid keyword to search"
        return suggestion_variable


def update_phone_number_db():
    """UI function to implement update_phone_number_db function"""
    update_phone_number_db = Tk()
    update_phone_number_db.resizable(False, False)
    update_phone_number_db.title("Update Phone number Database")
    update_phone_number_db.geometry("625x300")
    update_phone_number_db.config(bg="#474b47")
    phone_number_name = StringVar()
    phone_number = StringVar()
    string_name = StringVar()
    string_phone = StringVar()

    def phone_number_print():
        string_name1 = entry_phone_number_name.get()
        string_phone1 = entry_phone_number.get()
        global db_phone
        if len(string_phone1) == 13:
            create_and_update_phone_number_database(string_name1.lower(), string_phone1)
            if db_phone:
                pop1.config(fg="#00ff00")
                pop1.config(text="Data Entered Successfully!")
                window.update()
                update_phone_number_db.update()
            else:
                pop1.config(fg="#ff0000")
                pop1.config(text="User with same name already exists!")
                window.update()
                update_phone_number_db.update()

        else:
            pop1.config(fg="#ff0000")
            pop1.config(text="Enter Valid Phone number With Country Code!")
            window.update()
            update_phone_number_db.update()

    pop1 = Label(update_phone_number_db, text="", font=("Brandon Grotesque", 12), bg="#474b47")
    pop1.pack()
    un_lab1 = Label(update_phone_number_db, text="Enter name here", bg="#f3f9a7")
    un_lab1.pack()
    bl1 = Label(update_phone_number_db, text="", font=("Brandon Grotesque", 6), bg="#474b47")
    bl1.pack()
    entry_phone_number_name = Entry(update_phone_number_db, textvariable=phone_number_name)
    entry_phone_number_name.pack()
    bl2 = Label(update_phone_number_db, text="", font=("Brandon Grotesque", 6), bg="#474b47")
    bl2.pack()
    un1_label = Label(update_phone_number_db, text="Enter Phone number here +91", bg="#f3f9a7")
    un1_label.pack()
    bl3 = Label(update_phone_number_db, text="", font=("Brandon Grotesque", 6), bg="#474b47")
    bl3.pack()
    entry_phone_number = Entry(update_phone_number_db, textvariable=phone_number)
    entry_phone_number.pack()
    bl4 = Label(update_phone_number_db, text="", font=("Brandon Grotesque", 6), bg="#474b47")
    bl4.pack()
    button_submit = Button(update_phone_number_db, text="SUBMIT", command=phone_number_print)
    button_submit.pack()
    update_phone_number_db.mainloop()


def open_history():
    """Opens User History file"""
    os.startfile("UserHistory.txt")


def update_all_database():
    """Main UI container for updating database"""
    all_db = Tk()
    all_db.resizable(False, False)
    all_db.title("UPDATE DATABASE")
    all_db.geometry("525x500")
    all_db.config(bg="#474b47")
    Button(all_db, text="UPDATE PHONE NUMBER ", command=update_phone_number_db, bg="#f3f9a7",
                            font=("Brandon Grotesque", 12)).place(x=135, y=280)
    Label(all_db, text="\nSELECT DATABASE TO BE UPDATED\n", bg="#474b47", fg="#ffffff",
                          font=("comic sans ms", 15)).place(x=37, y=100)

    all_db.mainloop()


def update_suggestion():
    """Used to automatically submit data from search bar"""
    window.after(100, update_suggestion)
    tet2 = search_box_variable.get()
    suggestion_query = update_suggestion_arg(tet2.lower())
    if suggestion_query != "Please Enter a\n Valid keyword to search":
        search_box_variable1.set("Suggestions from your search : \n'" + tet2 + "' \n Command : " + suggestion_query)
    else:
        search_box_variable1.set("Enter Valid Keyword to Search")


iris_task_desc = ["-to open new instance",
                  "of notepad",
                  "-to play music from",
                  "your system",
                  "-to get top 5",
                  "national news",
                  "-to get current date &",
                  "time of your system",
                  "-to switch current",
                  "window",
                  "-to open the command",
                  "prompt",
                  "-to send whatsapp msg",
                  "(login whatsapp-web req)",
                  "-to play video on",
                  "youtube",
                  "-to hear random",
                  "jokes",
                  "-to hear inspirational",
                  "quotes",
                  "-to find your current",
                  "location using IP",
                  "-to take screenshot",
                  "of current screen",
                  "-to read a PDF from",
                  "your system",
                  "-to do vocal",
                  "calculations",
                  "-to get current temp",
                  "of a city",
                  "-to get charging %",
                  "of your system",
                  "-to get your network",
                  "speed (15sec)",
                  "-to translate your ",
                  "voice in hindi",
                  "-to set remainder",
                  "for particular event",
                  "-to write article with",
                  "your voice in notepad",
                  "-to play game",
                  "(rock-paper-scissors)",
                  "-to get information ",
                  "about I.R.I.S.",
                  "-to change language to",
                  "(English/Hindi/Gujarati)",
                  "-to stop IRIS",
                  "and close the application",
                  "-to type with your voice",
                  "in real time",
                  "-to search particular",
                  " thing on google"]

iris_task_list = ["Open Notepad",
                  "Play Music",
                  "News",
                  "Current Time or Time",
                  "Switch Window",
                  "Open Command Prompt",
                  "Send WhatsApp Message",
                  "Play Video On YouTube",
                  "Tell Me a Joke",
                  "Inspire Me",
                  "Show My Location",
                  "Take ScreenShot",
                  "Read PDF",
                  "Calculate This",
                  "Temperature or Weather",
                  "Power or Battery",
                  "Network Speed",
                  "Translate from Hindi",
                  "Remember that",
                  "Write Article",
                  "Play a Game",
                  "About You",
                  "Change Language",
                  "Sleep (Exit) ",
                  "Speak and Type",
                  "Search on Google"]

'''--------------------------------------------------------------------------------------------------------------------
----------------------------------------Logic for Executing various tasks----------------------------------------------
---------------------------------------------------------------------------------------------------------------------'''

if __name__ == '__main__':
    conn1 = sqlite3.connect('MailDatabase.db', check_same_thread=False)
    conn2 = sqlite3.connect('PhoneNumberDatabase.db', check_same_thread=False)

    window.title("Intelligent and Robust Information System(IRIS)")
    window.config(bg="#474b47")
    window.geometry("1350x740")
    l1 = Label(window, textvariable=user_says, font=("comic sans ms", 18), justify="left", bg="#474b47",
               fg="white").place(x=27, y=30)

    f1 = Frame(window, height=530, width=860, borderwidth=3, bg="#86c232", relief=SUNKEN).place(x=30, y=120)

    iris_says.set("IRIS")
    iris_says_lab = Label(f1, font=("comic sans ms", 20), bg="#86c232", justify="left", textvariable=iris_says).place(
        x=40, y=125)

    # Start button using threading
    start_button = Button(window, text="Start", command=lambda: threading.Thread(target=full_start).start(),
                          font=("comic sans ms", 12)).place(x=30, y=670)
    # Update Contacts
    update_database_button = Button(window, text="Update Contacts", font=("comic sans ms", 12),
                                    command=update_all_database).place(x=250, y=670)

    history = Button(window, text="History", font=("comic sans ms", 12),
                     command=lambda: threading.Thread(target=open_history).start()).place(x=560, y=670)
    # Exit button to destroy window
    exit_button = Button(window, text="Exit", font=("comic sans ms", 12),
                         command=lambda: threading.Thread(target=destroy_window()).start()).place(x=835, y=670)

    f2 = Frame(window, height=680, width=415, borderwidth=3, bg="#86c232", relief=SUNKEN).place(x=910, y=30)

    search_box = Label(f2, text="Search BOX", font=("comic sans ms", 20), bg="#86c232").place(x=1040, y=35)
    search_box_entry = Entry(f2, textvariable=search_box_variable, font=("comic sans ms", 18), relief=SUNKEN,
                             justify="center", fg="#ffffff",
                             width=20, background="#474b47").place(x=940, y=90)
    update_suggestion()
    search_box_suggest = Label(f2, textvariable=search_box_variable1, font=("comic sans ms", 14), justify="center",
                               bg="#f3f9a7", width=27).place(x=925, y=145)
    mylist = Listbox(f2, height=9, font=("comic sans ms", 16), width=22, relief=GROOVE, justify="center")

    list_index = []


    def list_index_generator():
        list_index.clear()
        window.update()
        for i in range(300000):
            r = random.randint(0, len(iris_task_list)-1)
            if r not in list_index:
                list_index.append(r)


    def list_generator_update():
        list_index_generator()
        window.after(15000, list_generator_update)
        mylist.delete(0, END)
        for j in range(3):
            if list_index[j] == 0:
                mylist.insert(END, iris_task_list[list_index[j]])
                mylist.itemconfigure(END, bg="#474b47", fg="white")
                mylist.insert(END, iris_task_desc[list_index[j]])
                mylist.itemconfigure(END, bg="#f3f9a7")
                mylist.insert(END, iris_task_desc[list_index[j] + 1])
                mylist.itemconfigure(END, bg="#f3f9a7")
            else:
                mylist.insert(END, iris_task_list[list_index[j]])
                mylist.itemconfigure(END, bg="#474b47", fg="white")
                mylist.insert(END, iris_task_desc[list_index[j] * 2])
                mylist.itemconfigure(END, bg="#f3f9a7")
                mylist.insert(END, iris_task_desc[list_index[j] * 2 + 1])
                mylist.itemconfigure(END, bg="#f3f9a7")


    list_index.clear()
    list_generator_update()
    mylist.place(x=940, y=255)
    window.mainloop()
