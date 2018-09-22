# 20 de setembro de 2018
# Mateus Israel


class Fila:
	def __init__(self):
		self.fila = []

	def entrar(self, nome):
		self.fila.append(nome)

	def sair(self):
		self.fila.pop(0)

onibus = Fila()

print("Pessoas na fila:")
onibus.entrar('Tiago')
onibus.entrar('Monica')
onibus.entrar('Leila')
onibus.entrar('Rafaela')

cont = 0
for pes in onibus.fila:
	cont += 1 
	print(cont, pes)

print("\n"
	"Fim do programa")



### Receber pessoas por input ###