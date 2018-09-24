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
