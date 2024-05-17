from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
from styles import estilosmenu
from menu import Menu
import threading
class Opciones(QMainWindow):


    def setup_ui(self):
        #para fijar tamaño es set_fixed_size(x,y)
        self.set_fixed_size(1080,640)
        self.window_icon = QIcon ("logo2.jpg")
        self.window_title='Archie'
        #self.size = QSize(1000,640)
        
      
        self.root_layout = QVBoxLayout()
        
        self.frame1 = QFrame()
        self.frame2 = QFrame()



        self.root_layout.add_widget(self.frame1,20)
        self.root_layout.add_widget(self.frame2,80)


        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)

        self.set_central_widget(self.widget)


        self.style_sheet = estilosmenu
        self.gifframe()


    def inputsframe (self,k):
        self.labeltext = QLabel(f"Hola {k}, selecciona una de las\nsiguientes opciones:", self, object_name = "ayuda")
        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.add_widget(self.labeltext)
        self.frame1.set_layout(self.inputs_layout)
        self.labeltext.font = 'Pixel-Art'
        self.labeltext.geometry = QRect (40, 40, 50, 950 )
        
        #if bandera == True:
        #   t = threading.Timer(2, nombre1(k))
        #    t.start()


    
    def gifframe (self):

    
        self.label = QLabel(self)
        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.add_widget(self.label)
        self.frame2.set_layout(self.inputs_layout)
        self.movie = QMovie("2GU.gif")
        self.label.set_movie(self.movie)
        self.movie.start()
        self.label.geometry = QRect (100,130,450,450)


        self.op1 = QPushButton ("Tramitacion\nCorrespondencia...", self, object_name = "op1")
        self.inputs_layout1 = QVBoxLayout()
        self.inputs_layout1.add_widget(self.op1)
        self.frame2.set_layout(self.inputs_layout1)
        self.op1.geometry = QRect (600,170,330,100)
        self.op1.font = 'Pixel-Art'
    
   
        self.op2 = QPushButton ("Control De\nDocumentos...", self,object_name = "op2")
        self.inputs_layout2 = QVBoxLayout()
        self.inputs_layout2.add_widget(self.op2)
        self.frame2.set_layout(self.inputs_layout2)
        self.op2.geometry = QRect (600,320,330,100)
        self.op2.font = 'Pixel-Art'
    
        
        self.op3 = QPushButton ("Organizacion", self,object_name = "op3")
        self.inputs_layout3 = QVBoxLayout()
        self.inputs_layout3.add_widget(self.op3)
        self.frame2.set_layout(self.inputs_layout3)
        self.op3.geometry = QRect (600,470,330,100)
        self.op3.font = 'Pixel-Art'

    
        """
        self.label.geometry = QRect (40, 120, 500 , 500)
        
        
        """
        self.labelvol = QPushButton (self,object_name = "vol")
        self.labelvol.pixmap = QPixmap ("volumen.png").scaled(50,50)
        self.labelvol.geometry = QRect(40,570,50,50)



"""
import sys
app = QApplication (sys.argv)
opciones=Opciones()
opciones.setup_ui()
opciones.show()

sys.exit(app.exec())

"""




    

#ejecutar aplicacion


