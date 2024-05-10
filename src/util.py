
import google.generativeai as genai
import google.ai.generativelanguage as glm
import re

class RegEx(object):

	line = ""
	need_bracket_inline = 0
	in_class = 0
	index = -1
	n_lines = 0
	classes = None
	lines = None

	def __init__(self, lines):
		self.classes = []
		
		self.lines = lines
		self.n_lines = len(lines)
		self.line = lines[0]

	def new(self, pattern, repl):
		last_line = self.line
		self.line = re.sub(pattern, repl, self.line)
		return last_line != self.line

	def exist(self, pattern):
		return re.search(pattern, self.line) != None

	def result(self):
		return '\n'.join(self.lines)
	
	def next(self):
		self.lines[self.index] = self.line
		if self.index == self.n_lines-1:
			return False
		
		self.index += 1
		self.line = self.lines[self.index]
		return True



#FUNÇÕES UTEIS PARA O PROJETO



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
    return model.generate_content(texto)

def cria_Schema():
        
    frase = glm.Schema(
    type = glm.Type.OBJECT,
        properties = {
            'numero':  glm.Schema(type=glm.Type.INTEGER),
            'descricao':  glm.Schema(type=glm.Type.STRING)
        },
        required=['numero', 'descricao']
    )
    frases = glm.Schema(
        type=glm.Type.ARRAY,
        items=frase
    )
    traducao = glm.Schema(
        type = glm.Type.OBJECT,
        properties = {
            'numero':  glm.Schema(type=glm.Type.INTEGER),
            'descricao':  glm.Schema(type=glm.Type.STRING)
        },
        required=['numero', 'descricao']
    )

    traducoes = glm.Schema(
        type=glm.Type.ARRAY,
        items=traducao
    )

    dica = glm.Schema(
        type = glm.Type.OBJECT,
        properties = {
            'numero':  glm.Schema(type=glm.Type.INTEGER),
            'descricao':  glm.Schema(type=glm.Type.STRING)
        },
        required=['numero', 'descricao']
    )

    dicas = glm.Schema(
        type=glm.Type.ARRAY,
        items=dica
    )

    add_to_database = glm.FunctionDeclaration(
        name="data_base",
        description=textwrap.dedent("""\
            Dicas para o usuário usar como resposta em uma conversa.
            """),
        parameters=glm.Schema(
            type=glm.Type.OBJECT,
            properties = {
                'frases': frases,
                'traducoes': traducoes,
                'dicas': dicas
            }
        )
    )

    return add_to_database