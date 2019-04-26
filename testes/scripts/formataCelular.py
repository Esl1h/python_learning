#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Exemplo de como formatar um número de celular usando .format()
#- Marcio Luís Siqueira - 26/03/2014


numeroCelular = input('Digite o número do Telefone Celular: ' )

try:
	if len(numeroCelular) != 11:
		raise ValueError
	else:
		numeroCelular = int(numeroCelular)# se contiver letras causa um ValueError
		numeroCelular = str(numeroCelular)
		celular = numeroCelular
		telFormatado = '({}) {}-{}-{}'.format(celular[0:2],
							celular[2] ,celular[3:7], celular[7:])
		print(telFormatado)

except ValueError:
	if len(numeroCelular) == 0:
		print('Você não digitou o número')
	else:
		print('Número inválido, o número precisa ter 11 números inteiros')

