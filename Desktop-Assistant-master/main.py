import os
import webbrowser
import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr

print('Initializing Jarvis')
Master='Abhishek'
# speak function will pronounce the speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function function will wish you on the initializing of jarvis
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning '+Master) 
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon '+ Master)

    else:
        speak('Good Evening' + Master)
    

#Function will take command from microphone
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        audio=r.listen(source)

    try:
        print('Recognizing..')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print('Say that again please')
        query=None

    return query 

#Main programe starts here

speak('Initializing Jarvis...')
wishMe()
speak("how can i help you {}".format(Master))
query=takeCommand()

# logic

if query is None:
    speak('{} Please say something to do'.format(Master))

elif 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak(results)

elif 'open youtube' in query.lower():
    urL='youtube.com'
    mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
    webbrowser.get('firefox').open_new_tab(urL)


elif 'open stack overflow' in query.lower():
    urL='stackoverflow.com'
    mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
    webbrowser.get('firefox').open_new_tab(urL)


elif 'open google' in query.lower():
    urL='google.com'
    mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
    webbrowser.get('firefox').open_new_tab(urL)


elif 'open whatsapp' in query.lower():
    urL='https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjw8cOQgczxAhVDxzgGHX1-Dz0QFjAAegQICRAD&url=https%3A%2F%2Fweb.whatsapp.com%2F&usg=AOvVaw1V09js0t2A_u6GXzP1jPsR'
    mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
    webbrowser.get('firefox').open_new_tab(urL)

elif 'open firefox' in query.lower():
    codePath="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    os.startfile(codePath)

elif 'the time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{Master} the time is {strTime}")

elif 'open code' in query.lower():
    codePath="C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

else:
    speak("{} This functionality is not define on me".format(Master))