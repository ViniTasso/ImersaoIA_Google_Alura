
import os
import textwrap
import json
from src import util
import google.generativeai as genai
import google.ai.generativelanguage as glm



#FUNÇÕES



def texto_padrao_dicas(texto, idioma="inglês"):
    """
    Descrição:
        Esta função gera um texto padrão para solicitar ao modelo de geração de texto que 
        forneça três opções de resposta para uma determinada frase em um idioma específico. 
        O texto também inclui um exemplo de como o resultado deve ser apresentado, com as 
        respostas e suas traduções correspondentes.

    Parâmetros:
        - `texto`: A frase para a qual se deseja gerar opções de resposta.
        - `idioma`: O idioma em que a resposta deve ser gerada (padrão é "inglês").

    Retorno:
        - Uma string contendo o texto padrão com as instruções para gerar opções de resposta.
    """
    return f"""
Me de 3 opções de resposta para responder a seguinte frase: \n
{texto} \n
A resposta escreva em {idioma} e a tradução em português.
Siga o exemplo de resultado que eu espero: 
Resposta 1: texto; 
Traducao 1: texto; 
Resposta 2: texto; 
Traducao 2: texto;
Resposta 3: texto;
Traducao 3: texto; 
Substitua a palavra texto pelo resultado obtido. Mostre também um tópico de "Dicas:"
"""

def possiveis_respostas(texto):
    """
    Descrição:
    E   sta função utiliza o modelo de geração de texto para gerar opções de resposta, 
    traduções e dicas com base em um texto padrão.

    Parâmetros:
        - `texto`: A frase para a qual se deseja gerar opções de resposta.

    Retorno:
        - Um dicionário contendo as opções de resposta, traduções e dicas.

    Frase utilizada no google,
    Exemplo de entrada e saída:

        Como eu posso responder a seguinte frase em francês "Bonjour!", me de 3 opções de 
        resposta e siga o exemplo de resultado
        Resposta 1: texto;
        Traducao 1: texto;

        Resposta 2: texto;
        Traducao 2: texto;

        Resposta 3: texto;
        Traducao 3: texto;

        Substitua a palavra texto pelo resultado obtido.

        Mostre também um tópico de "Dicas:"

    RESPOSTA DO GOOGLE

        Resposta 1: Bonjour!
        Tradução 1: Olá!
        Resposta 2: Salut!
        Tradução 2: Oi!
        Resposta 3: Coucou!
        Tradução 3: Alô!
        Dicas:
        "Bonjour!" é a forma mais comum e educada de dizer "olá" em francês.
        "Salut!" é uma forma mais informal e é usada entre amigos ou familiares.
        "Coucou!" é uma forma ainda mais informal e é usada entre pessoas muito próximas.

    """
    modelAI = model
    resposta = modelAI.generate_content(texto_padrao_dicas(texto=texto, idioma=idioma))
    #print("O primeiro retorno foi:\n"+resposta.text)

    resposta = modelAI.generate_content(textwrap.dedent(
        texto_padrao_JSON_dicas(resposta.text)
    ))
    #print(json.dumps(json.loads(resposta.text), indent=3))

    return json.loads(resposta.text)

def texto_padrao_JSON_dicas(texto):
    """
    Descrição:
        Esta função gera um texto padrão com instruções para retornar um JSON descrevendo as 
        respostas de frases, as traduções e as dicas com base em um texto fornecido.

    Parâmetros:
        - `texto`: O texto a ser incluído nas instruções.

    Retorno:
        - Uma string contendo o texto padrão com as instruções para retornar um JSON.

    """
    return """\
Por favor retorne JSON descrevendo as respostas de frases, as traduções e as dicas desse texto usando o seguinte schema: 

{"frase": list[FRASE], "traducao":list[TRADUCAO], "dicas":list[DICAS}

FRASE = {"numero": int, "descricao": str}
TRADUCAO = {"numero": int, " descricao ": str}
DICA = {"numero": int, descricao ": str}

Todos os campos são necessários

Importante: Só retorne um único texto valido de JSON.

Aqui está o conteúdo:\n

""" + texto
    """_summary_
        Cria modelo que permite ser usado como tool no generate e os resultados 
        já são inseridos conforme solicitado.        
    """

def modelo_dicas_schema(texto):
    """
    
    Descrição:
        Esta função não está implementada no código fornecido. Ela parece ser destinada a criar 
        um modelo baseado em expressões regulares para processar texto, mas atualmente retorna 
        uma string vazia.

    """
    modelAI = model
    add_to_database = util.cria_Schema()
    modelAI = modelAI = genai.GenerativeModel(
        model_name='models/gemini-1.5-pro-latest',
        tools = [add_to_database])

    result = modelAI.generate_content(f"""
        Adicione as frases de respostas, as traduções e as dicas, desse texto para dentro desse banco de dados:

        {texto}
        """,
        # Force a function call
        tool_config={'function_calling_config':'ANY'})

    fc = result.candidates[0].content.parts[0].function_call
    assert fc.name == 'add_to_database'
    print(json.dumps(type(fc).to_dict(fc), indent=3))
    return fc

def modelo_dica_regex(text):
    """
    Descrição:
        Esta função não está implementada no código fornecido. 
        
        Ela parece ser destinada a criar um modelo baseado em expressões regulares para 
        processar texto usando funções de regex.

    Parâmetros:
        - `text`: O texto da pergunta a ser gerada.

    Retorno:
        - A ideia e gerar um retorno estruturado e até transformado em lista de cada tópico.
    
    """
    reg = text.splitlines()
    regex = util.RegEx(reg)
    return ""

def unica_pergunta(text):
    """
    Descrição:
        Esta função utiliza o modelo de geração de texto para fazer uma pergunta com base no texto fornecido.

    Parâmetros:
        - `text`: O texto da pergunta a ser gerada.

    Retorno:
        - Uma string contendo a pergunta gerada pelo modelo.

    """
    modelAI = model
    resposta = modelAI.generate_content(text)
    return resposta.text

def validaConversa(texto):
    """
    Descrição:
        Esta função faz uma pergunta ao usuário para validar se um determinado texto está no idioma especificado.

    Parâmetros:
        - `texto`: O texto a ser validado.

    Retorno:
        - Um valor booleano indicando se o texto está no idioma especificado (True) ou não (False).
    """
    resposta = unica_pergunta(f"O texto {texto}, está no idioma {idioma}? \nResponda apenas sim ou não.")
    if "sim" in str.lower(resposta):
        return True
    else:
        return False

def chat_principal():
    """
    Função responsável por iniciar o módulo de conversação.

    Esta função inicia uma conversa interativa em um idioma escolhido pelo usuário, permitindo 
    a prática de conversação sobre um determinado assunto. Durante a conversa, o usuário pode 
    solicitar dicas sobre o que responder, obter traduções de frases e encerrar a conversação.

    Returns:
        None
    """
    print("Bem vindo ao módulo de conversa!\n \n Vamos aprender um idioma na prática??")
    print("Escolha um assunto para conversar!")
    #ainda não esta funcionando
    
    chat = model.start_chat(history=[]) #passa uma lista vazia

    print(f"Essa conversa deverá ser em {idioma} e você pode usar algumas ferramentas, \
veja quais são elas:\n      - Digite dica para receber dicas do que \
responder na conversa.\n      - Digite traduza para ver a tradução da conversa.\
\n      - Digite fim para sair do exercício de conversação.\n\n")
    
    
    nivel = "básico"
    assunto = "quem esta se conhecendo"

    response = chat.send_message(f"Inicie uma conversa no nível {nivel} sobre {assunto}, \
                                 no idioma {idioma}, nós nos conhecemos agora!")
    print("Dona Gemini: "+chat.history[-1].parts[0].text)

    prompt = input(f"Sua vez, bom esstudo de {idioma}: ")
    while prompt != "fim":
        if not (prompt == "dica" or prompt == "traduza"):
            response = chat.send_message(prompt, stream=True)
            print("Dona Gemini: ")
            for chunk in response:
                print(chunk.text)
            if validaConversa(chat.history[-1].parts[0].text):
                response = chat.send_message("Mantenha a conversa lingua "+idioma)
        prompt = input("diga algo: ")
        if validaConversa(prompt):
            if not (prompt == "dica" or prompt == "traduza" or prompt == "fim"):
                print("SISTEMA: Se desejar trocar de idioma, digite 'fim' para sair desta conversa!")
        ultimaFrase = chat.history[-1].parts[0].text
        if prompt == "dica":
            dicas = possiveis_respostas(texto=ultimaFrase)
            j = 0
            for i in range(3):
                print("Opção {}: {}.".format(i+1 ,dicas["frase"][i]["descricao"]))
            
            print("escolha uma das dicas para você utilizar: ")
            j = int(input())
            if not (j > len(dicas["frase"][i]["descricao"])):
                prompt = dicas["frase"][j-1]["descricao"]
        if prompt == "traduza":
            result = unica_pergunta("Traduza a seguinte frase para o português: {}".format(ultimaFrase))
            print("A tradução da frase {} é a seguinte: \n {}".format(
                result, ultimaFrase))




"""
    Função principal que inicia o programa de estudo de idiomas.

    Esta função solicita ao usuário que escolha um idioma para estudar e um tipo de estudo,
    como treinamento de conversação, e inicia a interação de acordo com as escolhas feitas.

    Parâmetros:
    - Nenhum parâmetro é necessário.

    Retorna:
    - Nenhum valor é retornado explicitamente, pois a função interage com o usuário e inicia outras funções
      conforme as escolhas feitas.

    """

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

idioma = ""

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
        idioma = linguas[resultado - 1]
        break



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

print("Qual vai ser o nosso estudo hoje?")
print("1- Treinar conversação.")
print("0- Para SAIR!\n")
print("Outros modelos serão implementados em breve!")

resposta = -1
while(resposta != 0):
    try:
        resposta = int(input())
    except:
        print("Resposta não permitida")
    if (resposta == 1):
        chat_principal()
        resposta = 0

#ler o o arquivo /data/profile.csv
#colocar os dados do usuário nas variáveis globais.

#fornecer as opções para o usuário escolher

#conversar com a Dona Gemini
#chamar funções talking

#revisão de coisas estudadas
#chamar flashcard

#aprender palavras em contexto
#chamar função guide