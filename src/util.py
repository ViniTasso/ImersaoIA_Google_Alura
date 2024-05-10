#FUNÇÕES UTEIS PARA O PROJETO QUE NÃO PRECISAM SER INSTANCIADAS


#Função para converter texto em voz
    #1
        #from gtts import gTTS #lib com ferramentas CLI para conversão de texto em voz do G. Translate
        #from playsound import playsound
def text_to_speech(texto):
    """
    speech = gTTS(text=texto)
    speech.save('media/audio.mp3')
    playsound('media/audio.mp3')
    """

def unique_response(model, texto):
    model = genai.GenerativeModel("models/gemini-1.0-pro")
    return model.generate_content(texto)