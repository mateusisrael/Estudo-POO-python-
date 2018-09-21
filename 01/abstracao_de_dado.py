class Fila:


	def __init__(self):		# Isso é um método que "traz" atributos dinâmicos
		self.fila = []

	def entrar(self, nome):
		self.fila.append(nome)		# append() = função no python para adicionar valores na lista.

	def sair(self):
		self.fila.pop(0)			# pop()	= função para tirar valores da lista


# mercado = Fila()			>	Instância a Fila
# mercado.entrar('Eduardo')	>	Eduardo "entrou" na fila	
# mercado.entrar('Luiz')	> 	Luiz "entrou" na fila
# mercado.fila()  			>  Mostra a ordem da fila