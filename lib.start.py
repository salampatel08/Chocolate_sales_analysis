import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("muh me leke dikha")

    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

try:
    text=r.Recognize_google(audio,language="hi-IN")
    print("tu bola",text)
except Exception as e:
    print("error",e)