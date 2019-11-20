#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:34:16 2016

@author: esl1h
"""
valcusto = input ("Qual o valor de custo do produto?: R$")
valperc = input ("Qual a porcentagem que deseja acrescentar para vender o produto?: %")
#
lucro = int(valperc) * int(valcusto) / 100.0
print( "Valor a lucrar: R$",lucro)
print( "Valor para venda do produto: R$",int(valcusto) + lucro )
