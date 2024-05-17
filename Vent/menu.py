from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QMovie, Qt, QPixmap, QImage, QPicture
from PySide6.QtCore import *
from __feature__ import snake_case, true_property 
from styles import estilosmenu
import threading
import pygame
import keyboard





class Menu(QMainWindow):

    def setup_ui(self):
        self.set_fixed_size(1080,640)
        #para fijar tamaño es set_fixed_size(x,y)
        #self.set_fixed_size(1080,640)
        self.window_icon = QIcon ("logo2.jpg")
        self.window_title='Archie'

    

        self.framearchie = QFrame(self)
        self.framearchie.geometry = QRect (0,0,540,640)
     

        self.frameinput = QFrame (self)   
        self.frameinput.geometry = QRect (540,0,540,640)
        

        self.style_sheet=estilosmenu
       

     
        self.inputsframe()
        self.gifframe()




    def repro (self):
        pygame.mixer.init()
        self.sonido = pygame.mixer.Sound("mar1.mp3")
        self.sonido.play()
        self.sonido.set_volume(0.1)

    def pausar(self):
        self.sonido.pause()

                

    def inputsframe (self):
        self.inputTexto = QLineEdit(self.frameinput)
        self.inputTexto.font = 'Pixel-Art'
        self.inputTexto.geometry = QRect(0,400,300,60)
        self.inputTexto.max_length=9

        self.boton1 = QPushButton ("Continuar...",self.frameinput)
        self.boton1.geometry = QRect (100,100,330,100)
        self.boton1.font = 'Pixel-Art'
        

        self.boton2 = QPushButton (self.frameinput)
        self.boton2.geometry = QRect (300,400, 100, 60)
        self.boton2.font = 'Pixel-Art'
        self.boton2.icon = QIcon ('microfono1.png')
        self.boton2.iconSize=QSize(20, 20)

        
    def gifframe (self):
        self.label = QLabel(self.framearchie)
        self.label.geometry = QRect(40,80,480,400)
        self.movie = QMovie("archie.gif")
        self.label.set_movie(self.movie)
        self.movie.start()

        self.labelvol = QPushButton (self.framearchie)
        self.labelvol.geometry = QRect(40,570,50,50)
        self.labelvol.pixmap = QPixmap ("volumen.png").scaled(50,50)

    

  
    

#ejecutar aplicacion
"""
import sys
app = QApplication (sys.argv)
menu=Menu()
menu.setup_ui()
menu.show()



sys.exit(app.exec())

"""






