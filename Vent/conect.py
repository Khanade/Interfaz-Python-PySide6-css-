from menu import Menu
from ventana2 import Opciones
from dialogo2 import Voz
from PySide6.QtWidgets import QApplication
from __feature__ import snake_case, true_property
import speech_recognition as sr
from voz import Grabarvoz
from dialogo import run_mike, nombre1, pausa
import threading
import pygame
import keyboard
import pyttsx3





pygame.init()

pygame.mixer.music.load('menusong.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)


class Conexion:
    
    def __init__(self):

        self.menu=Menu()
        self.ventana2 = Opciones()
        self.menu.setup_ui()
        self.ventana2.setup_ui()
        self.grabacion=Grabarvoz()


       
        self.menu.boton1.clicked.connect(self.abriropciones)
        self.menu.boton2.clicked.connect(self.gnombre)
        
        
    def abriropciones(self):
        self.menu.repro()
        self.menu.hide()
        self.ventana2.show()
        self.ventana2.inputsframe(self.menu.inputTexto.text)
        pausa()
        pausa()
        pausa()
        pausa()
        t = threading.Timer(1, nombre1(self.menu.inputTexto.text))
        t.start()
 
   
    def gnombre (self):
        r= sr.Recognizer()

        with sr.Microphone() as recurso:

            print ("Dime algo...")
            audio = r.listen(recurso)

            try:
                texto = r.recognize_google(audio, language= 'es-ES')
                #print("Esto es lo que has dicho: {}".format(texto))
                retorno = texto
                self.ventana2.inputsframe(retorno)
                print("")
                #with open ("audio.wav","wb") as fichero:
                    #fichero.write(audio.get_wav_data())
            except:
                print("Lo siento. No entendí, intenta de nuevo") 
                
                return 0

        self.menu.repro()
        self.menu.hide()
        self.ventana2.show()
        pausa()
        pausa()
        pausa()
        pausa()
        t = threading.Timer(1, nombre1(retorno))
        t.start()
        


        
   





import sys
app = QApplication (sys.argv)
main = Conexion()
main.menu.show()

t = threading.Timer(1, run_mike)
t.start()
sys.exit(app.exec())

