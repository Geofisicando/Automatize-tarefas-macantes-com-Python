import pyperclip

tags='linux ubuntu,terminal,geofísica,programação,geofisicando,'

opcao = input('Escolha c ou p: ')

if opcao=='c':
	novastags = 'linguagem c,c orientado a testes,tdd,'
elif opcao=='p':
	novastags = 'python,curso básico de python,'
else:
	print('Erro, opção desconhecida!')
	exit()

tags = tags+novastags

pyperclip.copy(tags)
input('Use ctrl+v para colar as tags ou enter para encerrar')

