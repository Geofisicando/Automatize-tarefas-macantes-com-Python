import pyperclip

msg1 = "Aproveite também para se inscrever no meu canal onde ensino programação em linguagem C orientado a testes https://www.youtube.com/watch?v=WDf6UWpKR60&t=9s"

msg2 = "Aproveite também para se inscrever no meu canal onde ensino programação em linguagem Python https://youtu.be/k6Os354BJVQ"

opcao = input('escolha c ou p: ')

if opcao == 'c':
	pyperclip.copy(msg1)
	input('Use ctrl+v para colar a mensagem ou enter para encerrar')
elif opcao == 'p':
	pyperclip.copy(msg2)
	input('Use ctrl+v para colar a mensagem ou enter para encerrar')
else:
	print('Erro, opção desconhecida!')
