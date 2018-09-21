from abstracao_de_dado import Fila

mercado = Fila()	# compartilhamos os estados entre todas as instancias
loterica = Fila()	#
banco = Fila()		#

banco.entrar('Eduardo')
loterica.entrar('Tiago')
mercado.entrar('David')


print('')
print("Loterica:", loterica.fila)
print("Banco:", banco.fila)
print("Mercado:", mercado.fila)

print("\n Fim do programa")