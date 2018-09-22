''' Mateus Israel
21 de setembro de 2018

Exercitando o uso de funções.
voar ou pousar. '''



def voar():
    print('voando\n')

def pousar():
    print('pousando\n')

comm = True
while comm != 'sair' and comm == True:
    comm = str(input('Digite um comando: '))
    if comm == 'voar':
        voar()
        comm = True

    elif comm == 'pousar':
        pousar()
        comm = True

    elif comm == 'sair':
        print('Saindo')
        exit()

    else:
        print('Comando inválido\n\n')
        comm = True
