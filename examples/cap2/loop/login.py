login_correto = 'Dirack'
senha_correto = '12345'

while True:
	login = input('Login: ')
	senha = input('Senha: ')

	if login != login_correto:
		print('Erro, login incorreto')
		continue
	elif senha != senha_correto:
		print('Erro, senha incorreta')
		continue
	else:
		print('Login realizado com sucesso!')
		break
