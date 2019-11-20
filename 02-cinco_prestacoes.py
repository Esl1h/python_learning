#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:21:37 2016
@author: esl1h
"""
print("Parcelamento de compras! Desculpe-me mas este programa só parcela em 5X hahaha")
compraparc = input("Qual o valor total das compras?: ")
#
parcela = int(compraparc) / 5.0
print("O cliente pagará as compras em 5 parcelas de R$",parcela," cada")
#
print( "Compreendendo em: ")
print( "\tNo ato da compra: ", parcela)
print( "\t30 dias: ", parcela)
print( "\t60 Dias: ", parcela)
print( "\t90 Dias: ", parcela)
print( "\t120 Dias: ", parcela)
