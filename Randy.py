import webbrowser
import speech_recognition as sr
import subprocess
import os
from gtts import gTTS
from playsound import playsound
from datetime import datetime
from googletrans import Translator, constants

months=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
days=['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
translator = Translator()

#Aqui coloca las direcciones de tus programas
Asistente="D:\Python\\asistentevirtual" #La ruta donde tienes el asistente y los audios, para que funcionen correctamente
Epic='C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
VSCode="C:\\Users\\rayul\AppData\Local\Programs\Microsoft VS Code\Code.exe"

r=sr.Recognizer()
playsound("D:\Python\\asistentevirtual\init.mp3")
while True:
    with sr.Microphone() as source:
        audio=r.listen(source)
        text=""
        if audio != None:
            try:
                text = r.recognize_google(audio)
                output="Lo siento, no entendí"
                print('Has dicho: {}'.format(text))
                
                if "auxilio" in text:
                    output=""
                    text=""
                    playsound(Asistente+"\help.mp3")


                if "Amazon" in text:
                    webbrowser.open('https://www.amazon.com.mx/')
                    output="Abriendo amazon"
                if "Google" in text:
                    if "Busca" in text:
                        webbrowser.open('https://www.google.com/search?q='+(text[text.upper().find("BUSCA")+6:]).replace(" ","%20"))
                        output="Buscando "+text[text.upper().find("BUSCA")+6:]+"en google"
                    else:
                        webbrowser.open('https://www.google.com/')
                        output="Abriendo google"
                if "YouTube" in text:
                    if "Busca" in text:
                        webbrowser.open('https://www.youtube.com/results?search_query='+(text[text.upper().find("BUSCA")+6:]).replace(" ","%20"))
                        output="Buscando "+text[text.upper().find("BUSCA")+6:]+"en youtube"
                    else:
                        webbrowser.open('https://www.youtube.com/')
                        output="Abriendo youtube"
                if "Facebook" in text:
                    webbrowser.open('https://www.facebook.com/')
                    output="Abriendo facebook"
                if "Telegram" in text:
                    webbrowser.open('https://web.telegram.org/k/')
                    output="Abriendo telegram"
                if "WhatsApp" in text or "what's up" in text:
                    webbrowser.open('https://web.whatsapp.com/')
                    output="Abriendo what's up"
                if "Epic" in text:
                    subprocess.call([Epic])
                    output="Abriendo epic games"
                if "Netflix" in text:
                    if "Busca" in text:
                        webbrowser.open('https://www.netflix.com/search?q='+(text[text.upper().find("BUSCA")+6:]).replace(" ","%20"))
                        output="Buscando "+text[text.upper().find("BUSCA")+6:]+"en netflix"
                    else:
                        webbrowser.open('https://www.netflix.com/')
                        output="Abriendo netflix"
                    
                if ("PROGRAMAR" in text.upper() or "DIESEL" in text.upper()):
                    subprocess.call([VSCode])
                    output="Abriendo visual studio code"

                if "Commando" in text:
                    os.system("start cmd") 
                    output="Abriendo cmd"

                if "Tiempo" in text:
                    d=datetime.now()
                    h=d.hour
                    tarde=" de la mañana"
                    if h>12:
                        h=h-12
                        tarde=" de la tarde"
                    m=d.minute
                    output=('Son las '+str(h)+' con '+str(m)+" minutos "+tarde)

                if "FECHA" in text.upper():
                    d=datetime.now()
                    output=('Hoy es '+str(days[d.weekday()])+' '+str(d.day)+' de '+str(months[d.month-1])+' del '+str(d.year ))

                if "TRADUCIR" in text.upper():
                    print(text[text.upper().find("TRADUCIR")+9:])
                    output=translator.translate(text[text.upper().find("TRADUCIR")+9:]).text
                
                
                if "TRANSLATE" in text.upper():
                    print(text[text.upper().find("TRANSLATE")+10:])
                    output=translator.translate(text[text.upper().find("TRANSLATE")+10:],dest="es").text
                    
                
                
                
                if output!="":
                    tts=gTTS(output,lang='es-us')
                    with open(Asistente+"\output.mp3","wb") as file:
                        tts.write_to_fp(file)
                    playsound(Asistente+"\output.mp3")
                    os.remove(Asistente+"\output.mp3")

            except:
                if text!="":
                    print('No entiendo')
                    playsound(Asistente+"\error.mp3")