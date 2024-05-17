import pyttsx3

class Voz():

	def pausa():
		self.engine = pyttsx3.init()

		self.engine.say(" ")

		self.engine.runAndWait()
	def voz(self):
		self.engine = pyttsx3.init()

		self.engine.say("Hello, This is the test for the pyttsx3")

		self.engine.runAndWait()

	def saludo(self):

		self.engine = pyttsx3.init()

		self.engine.say("Hola, un gusto poder saludarte. Por favor dime tu nombre,  o escríbelo donde te señala nuestro asistente Archie")

		self.engine.runAndWait()



