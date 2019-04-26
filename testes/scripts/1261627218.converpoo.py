#!/usr/bin/env python
# -*-    coding:   iso8859-1    -*-
# Conversor de Temperaturas Celsius, Kelvin e Fahrenheit


import os

class Temp:
	def __init__ ( self ):     # na 1� vers�o era utilizado o contexto de execu��o que iniciava as fun��es janela() e loof(). Ex: if   __name__=='__main__':  main()
		self.janela()				#def main(): janela(); loof()
		self.loof()
		
	def celsius(self, c=None):  # m�todo respons�vel pelas opera��es de conven��es com Celsius
		self.con1 = c + 273
		self.con2 = (c * 9.) / 5. + 32
		print " A convers�o em Kelvin: %dK" % self.con1
		print " A convers�o em Fahrenheit: %.2f�F" % self.con2
		print " Digite 5 para reiniciar o menu!"
		
	def kelvin(self, k=None): # m�todo respons�vel pelas opera��es de conven��es com Kelvin
		self.con3 = k - 273
		self.con4 = ((k - 273) / 5.) * 9. + 32
		print " A convers�o em Celsius: %.2f�C" % self.con3
		print " A convers�o em Fahrenheit: %.2f�F" % self.con4
		print " Digite 5 para  reiniciar o menu!"
		
	def fahrenheit(self, f=None): # m�todo respons�vel pelas opera��es de conven��es com  Fahrenheit
		self.con5 = ((f - 32) / 9.) * 5.
		self.con6 = ((f - 32) / 9.) * 5. + 273
		print " A convers�o em Celsius: %.2f�C" %self.con5
		print " A convers�o em Kelvin: %.2fK"  %self.con6
		print " Digite 5 para reiniciar o menu!"
		
	def janela(self):	              # m�todo responsavel pelo menu no terminal
		if os.name == 'POSIX':   #troque 'POSIX' pelo nome do seu O.S, se for DOS use 'DOS'
			os.system('clear')      # o atributo 'system'  do modulo 'os' executa opera��es do sistema operacional, neste caso o argumento 'clear' ir� limpa o terminal no GNU/Linux ou *nix e no DOS seria 'cls'
		else:
			os.system('clear')
			print"---------------------------------------------------------------"
			print"  Conversor de Temperaturas: Celsius, Kelvin e Fahrenheit!"
			print"  Copyright(c)- Astdarkness(2004-2005)-by Alan Santos Teixeira"
			print"---------------------------------------------------------------"
			print"        Escolha uma das alternativas e tecle enter"
			print"\n"
			print"            1. Celsius para Kelvin e Fahrenheit"
			print"            2. Kelvin para Celsius e Fahrenheit"
			print"            3. Fahrenheit para Kelvin e Celsius"
			print"\n"
			print"            4. Sair deste programa"
			print"---------------------------------------------------------------"
			

	def loof(self):    #m�todo responsavel pelo loop  que espera o comando do usuario e executa a determinada op��o
		while 1:
								# Nos blocos 'if' � encontrados tratamentos de erros para determinado m�todo, isso impede do
			try:				#programa ser abortado por erro do usuario, caso  este entre com caracteres e use virgulas no n�meros o que seria uma tupla.
					self.x = input('> ')
			except:
					x = 0
			if self.x == 1:
				try:
					self.celsius(input('Digite um valor em Celsius:'))
				except TypeError:
					print "N�o use virgulas, somente ponto! Tente novamente."
					print " Digite 5 para reiniciar o menu!"
				except SyntaxError:
					print "Use somente ponto para n�meros reais n�o inteiros! ex: 3.3"
					print " Digite 5 para reiniciar o menu!"
				except NameError:
					print "Use n�meros somente!"
					print "Digite 5 para reiniciar o menu!"
			elif self.x == 2:
				try:
					self.kelvin(input('Digite um valor em Kelvin: '))
				except TypeError:
					print"N�o use virgulas, somente ponto! Tente novamente."
					print " Digite 5 para reiniciar o menu!"
				except SyntaxError:
					print "Use somente ponto para n�meros reais n�o inteiros! ex: 3.3"
					print " Digite 5 para reiniciar o menu!"
				except NameError:
					print "Use n�meros somente!"
					print "Digite 5 para reiniciar o menu!"
			elif self.x == 3:
				try:
						self.fahrenheit(input('Digite um valor em Fahrenheit: '))
				except TypeError:
					print"N�o use virgulas, somente ponto! Tente novamente."
					print " Digite 5 para reiniciar o menu!"
				except SyntaxError:
					print "Use somente ponto para n�meros reais n�o inteiros! ex: 3.3"
					print " Digite 5 para reiniciar o menu!"
				except NameError:
					print "Use n�meros somente!"
					print "Digite 5 para reiniciar o menu!"
			elif self.x == 4:
				print "Saindo..."
				break
			else:
				self.janela()
				
grau=Temp()  #inst�ncia��o da classe
