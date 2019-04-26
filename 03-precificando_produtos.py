#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:34:16 2016

@author: esl1h
"""
valcusto = input ("Qual o valor de custo do produto?: R$")
valperc = input ("Qual a porcentagem que deseja acrescentar para vender o produto?: %")
#
lucro = valperc * valcusto / 100
print "Valor a lucrar: R$",lucro
print "Valor para venda do produto: R$",valcusto + lucro


# MODO DO LIVRO PARA RESOLUÇÃO:
#
# valcusto =  = input ("Qual o valor de custo do produto?: R$")
# valperc = input ("Qual a porcentagem para vender o produto?: %")
#
# valperc = ( valperc /100.0 ) * valcusto
# venda = valcusto + valperc
# print "Valor para venda do produto é R$",venda
#
#