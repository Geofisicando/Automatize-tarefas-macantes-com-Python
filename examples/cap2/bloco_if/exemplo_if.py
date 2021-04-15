# Exemplo de utilização do bloco if

preco_ingresso=50

dinheiro_usuario = int(input('Quanto dinheiro vc tem: '))

if dinheiro_usuario < preco_ingresso:
	print('Vc NÃO poderá ir ao cinema')
	exit()

print('Vc poderá ir ao cinema')
