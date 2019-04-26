#!/usr/bin/python
# -*- coding: utf-8 -*-

#Exemplo de código python, por Gabriel Falcão <gabrielteratos@gmail.com>
#É necessário ter os binários sha1sum e md5sum em seu linux
#
#gera soma em um dos algoritmos de criptografia de uma via, definidos acima.
import commands

def gera_md5(valor):
	soma_md5=commands.getoutput("echo \""+valor+"\" | md5sum -t")
	soma_md5=soma_md5[:-3]
	return soma_md5
def gera_sha1(valor):
	soma_sha1=commands.getoutput("echo \""+valor+"\" | sha1sum")
	soma_sha1=soma_sha1[:-3]
	return soma_sha1
def choose_md5():
	nome=raw_input("Digite algo:\n")
	nome2=gera_md5(nome)
	print "Soma MD5 de \""+nome+"\":"
	print nome2
def choose_sha1():
	nome=raw_input("Digite algo:\n")
	nome2=gera_sha1(nome)
	print "Soma SHA1 de \""+nome+"\":"
	print nome2
opcao=1
while((opcao==1)or(opcao==2)):

	print "\n=====\nMENU\n=====\n"
	print "1) Gera MD5sum"
	print "2) Gera SHA1sum"
	print "3) SAIR\n"
	opcao=input("OPCAO:")
	if (opcao==1):
		choose_md5()
	elif (opcao==2):
		choose_sha1()

