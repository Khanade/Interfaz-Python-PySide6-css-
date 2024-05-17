import speech_recognition as Sr


class Grabarvoz():
        
    def grabar(self):
        r= Sr.Recognizer()

        with Sr.Microphone() as recurso:

            print ("Dime algo...")
            audio = r.listen(recurso)

            try:
                texto = r.recognize_google(audio, language= 'es-ES')
                print("Esto es lo que has dicho: {}".format(texto))
                retorno = texto
                print("Esto es lo que has dicho:"+retorno)
                #with open ("audio.wav","wb") as fichero:
                    #fichero.write(audio.get_wav_data())
            except:
                print("Lo siento. No entendí, intenta de nuevo") 
                
                return 0
    
           
        