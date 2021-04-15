# imposto = taxa*salario

salario_usuario = float(input('Qual o seu salário: '))
sexo_usuario = input('Qual o seu sexo (m/f): ')

taxa_m = 0.15
taxa_f = 0.10

if sexo_usuario == 'm':
	imposto = taxa_m * salario_usuario
elif sexo_usuario == 'f':
	imposto = taxa_f * salario_usuario
else:
	print('Erro, valor do sexo do usuário desconhecido')
	exit()

print('Imposto a pagar: '+str(imposto))
