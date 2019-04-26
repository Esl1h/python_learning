#!/usr/bin/python
HOME='/home/fabio/'

def linha():
	print '\n\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n\n'

def sobre():
	linha()
	print '\tEscrito por Fábio Berbert de Paula\n'
	print '\tE-mail: fabio@vivaolinux.com.br\n'
	print '\thttp://www.vivaolinux.com.br\n\n'
	print '\tLinux Solutions (www.linuxsolutions.com.br)\n'
	print '\twww.olinux.com.br - o portal Linux nacional'
	linha()
	raw_input('Tecle <ENTER> para continuar...')
	inicio()

def alterar():
	linha()
	nome = raw_input('Qual nome desejas alterar? ')
	f=open(HOME + '.agenda','r')
	novo = ""
	num = len(nome)
	for X in f.readlines():
		if X[0:num] == nome:
			nome = raw_input('Nome: ')
			fone = raw_input('Fone: ')
			novo = novo + nome + ' - ' + fone + '\n'
		else:
			novo = novo + X
	f.close()
	g=open(HOME + '.agenda','w')
	g.write(novo)
	g.close()
	inicio()


def excluir():
	linha()
	nome = raw_input('Qual nome desejas excluir? ')
	f=open(HOME + '.agenda','r')
	novo = ""
	num = len(nome)
	for X in f.readlines():
		if X[0:num] == nome:
			pass
		else:
			novo = novo + X
	f.close()
	g=open(HOME + '.agenda','w')
	g.write(novo)
	g.close()
	inicio()
	

def cadastrar():
	linha()
	nome = raw_input('Nome: ')
	fone = raw_input('Fone: ')
	f=open(HOME + '.agenda','a')
	f.write(nome + ' - ' + fone + '\n') 
	f.close()
	inicio()

def consultar():
	linha()
	f=open(HOME + '.agenda','r')
	lista = f.readlines()
	lista.sort()
	for X in lista:
		print X
	f.close()
	raw_input('\n\nTecle <<ENTER>> para continuar...')
	inicio()

def inicio():
	linha()
	print 'Selecione uma das opções abaixo:\n\n'
	print '\t(1) Cadastrar fone\n'
	print '\t(2) Consultar agenda\n'
	print '\t(3) Excluir registro\n'
	print '\t(4) Alterar registro\n'
	print '\t(5) Sobre\n'
	print '\t(6) Sair\n\n'
	num = raw_input('Opção: ')
	print num
	if num == '1':
		cadastrar()
	elif num == '2':
		consultar()
	elif num == '3':
		excluir()
	elif num == '4':
		alterar()
	elif num == '5':
		sobre()
	elif num == '6':
		exit	
	else:
		linha()
		print 'Opção inválida. Tente novamente...'
		inicio()

inicio()
