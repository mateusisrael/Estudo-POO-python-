'''
23 de setembro de 2018
Mateus Israel

Estudo de classes:
'''

class Estados:

    def __init__(self):
        self.estado = 'Neutro'

    def andar(self):
        self.estado = 'Andando'
        print(self.estado)

    def parar(self):
        self.estado = 'Parado'
        print(self.estado)

    def abastecer(self):
        self.estado = 'Abastecendo'
        print(self.estado)

carro = Estados()       # Para usar a classe, criamos antes uma instância

print('')               
print(carro.estado)     # Mostrar o estado atual do carro
carro.andar()           # Passando a função para o carro andar
carro.parar()           # Passando a função para o carro parar
carro.abastecer()       # E passando a função para o carro abastecer
print('')


print("Fim do programa")


'''
Nesse exercício tive dificuldade em passar os estados para o carro, pois não sabia que era 
necessário criar uma instâcia do objeto (carro).

Depois de criar a instância conseguir passar facilmente as funções.

'''
