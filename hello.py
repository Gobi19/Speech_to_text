import speech_recognition as sr
import pyaudio
s=sr.Recognizer()
with sr.Microphone() as src:
    print('Say something \n')
    audio=s.listen(src)
    try:
        txt=s.recognize_google(audio)
        print(txt)
    except:
        print('Couldnt catch wht u said')