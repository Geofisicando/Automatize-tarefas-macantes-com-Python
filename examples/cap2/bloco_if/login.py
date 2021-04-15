login_correto = 'Dirack'
senha_correto = '12345'

login = input('Login: ')
senha = input('Senha: ')

if login != login_correto:
	print('Erro, login incorreto')
	exit()
elif senha != senha_correto:
	print('Erro, senha incorreta')
	exit()

print('Login realizado com sucesso!')
