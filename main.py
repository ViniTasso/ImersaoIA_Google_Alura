import google.generativeai as genai

lingua = ""
while(True):
    print ("Qual lingua deseja estudar hoje?")
    linguas = ["Inglês", "Frances", "Alemão", "Espanhol", "Italiano"]
    
    for i in range(len(linguas)):
        print("Digite {} para {};\n".format(i+1, linguas[i]))

    resultado = 0
    try:
        resultado = int(input())
    except:
        print("Número invalido")

    if  resultado > 0 and resultado < len(linguas)+ 1:
        lingua = linguas[resultado - 1]
        break
    
genai.configure(api_key="")


""" Os Modelos disponíveis podem ser:
models/gemini-1.0-pro
models/gemini-1.0-pro-001
models/gemini-1.0-pro-latest       
models/gemini-1.0-pro-vision-latest
models/gemini-1.5-pro-latest       
models/gemini-pro
models/gemini-pro-vision
"""
model = genai.GenerativeModel("models/gemini-1.0-pro")
#response = model.generate_content("Write a story about a Magic world")
#print(response.text)


#response = model.generate_content('Tell me a story about a magic backpack', stream=True)
#for chunk in response:
#    print(chunk.text)


chat = model.start_chat(history=[]) #passa uma lista vazia

prompt = input("Esperando prompt: ")

while prompt != "fim":
      response = chat.send_message(prompt, stream=True)
      for chunk in response:
        print(chunk.text)
      prompt = input("Eai, o que quer dizer: ")


#    chat = model.start_chat()
#    response = chat.send_message("Hi, I have some questions for you.")
#    response.text





#ler o o arquivo /data/profile.csv
#colocar os dados do usuário nas variáveis globais.

#fornecer as opções para o usuário escolher

#conversar com a Dona Gemini
#chamar funções talking

#revisão de coisas estudadas
#chamar flashcard

#aprender palavras em contexto
#chamar função guide