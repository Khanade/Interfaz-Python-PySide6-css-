import pyttsx3

engine = pyttsx3.init() 
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def run_mike():
    talk("¡Hola! un gusto poder ayudarte, por favor dime tu nombre, o escríbelo donde te señala nuestro asistente Archie")
def nombre1(nom):
    talk("¡Hola!"+nom+"como podemos ayudarte... Trabajaremos lo mas rápido posible para ti.")
def pausa():
    talk ("")

bandera = True

if bandera == False:
    run_mike()
    nombre1()
    pausa()