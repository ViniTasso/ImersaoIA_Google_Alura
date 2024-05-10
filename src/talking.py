import google.generativeai as genai
import google.ai.generativelanguage as glm
import textwrap
import json
import util

#class Conversando_com_IA:
"""
disponibilizar alguns assuntos para o usuario escolher 

dentro do assunto, pedir para o bot iniciar a conversa. se clicar em cima mostrar tradução.

disponibilizar 3 opções de resposta para a frase mostrada pelo bot

dar a opção da pessoa escrever.

se clicar em cima das opções prontas, mandar para o bot

se digitar, mandar para o bot corrigir os erros com "você quis dizer, seria melhor se dizer"
dar a opção de aceitar ou digitar novamente

    """




def texto_padrao_dicas(self, texto, idioma="inglês"):
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

def possiveis_respostas(self, texto, idioma, modelAI):
    """
        Frase utilizada no google:

Como eu posso responder a seguinte frase em francês "Bonjour!", me de 3 opções de resposta e siga o exemplo de resultado
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
    resposta = modelAI.generate_content(texto_padrao_dicas(texto, idioma=idioma))
    print("O primeiro retorno foi:\n"+resposta.text)

    resposta = modelAI.generate_content(textwrap.dedent(
        talk.texto_padrao_JSON_dicas(resposta.text)
    ))
    print(json.dumps(json.loads(resposta.text), indent=3))


    return resposta.text
def texto_padrao_JSON_dicas(texto):
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

def modelo_dicas_schema(modelo, texto):

    add_to_database = util.cria_Schema()
    model = model = genai.GenerativeModel(
        model_name='models/gemini-1.5-pro-latest',
        tools = [add_to_database])

    result = model.generate_content(f"""
        Adicione as frases de respostas, as traduções e as dicas, desse texto para dentro desse banco de dados:

        {texto}
        """,
        # Force a function call
        tool_config={'function_calling_config':'ANY'})

    fc = result.candidates[0].content.parts[0].function_call
    assert fc.name == 'add_to_database'
    print(json.dumps(type(fc).to_dict(fc), indent=4))
    return fc

def modelo_dica_regex():
    return ""

def principal(idioma, model):
    print("Bem vindo ao módulo de conversa!\n \n Vamos aprender um idioma na prática??")
    print("Escolha um assunto para conversar!")
    #ainda não esta funcionando
            
    chat = model.start_chat(history=[]) #passa uma lista vazia

    prompt = input("Esperando prompt: ")

    while prompt != "fim":
        response = chat.send_message(prompt, stream=True)
        for chunk in response:
            print(chunk.text)
        prompt = input("Eai, o que quer dizer: ")
        if prompt == "dica":
            dicas = possiveis_respostas(chat.history[-1],idioma, model)
            print(dicas)
