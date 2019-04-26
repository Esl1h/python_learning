#!/usr/bin/python
# Calculo dos dias de vida
 
from datetime import date
 
atual = date.today()
Data = input('Digite o dia vc em que nasceu: ')
mes = input('Digite o mes em que vc nasceu: ')
Ano = input('Digite o ano em que vc nasceu: ')
 
total = date(atual.year,atual.month,atual.day) - date(Ano,mes,Data)
print "voce esta vivendo a:\nDias: %s\nAnos: %s\nMeses: %s\nSemanas: %s\n" %(total.days,total.days/365,total.days/30,total.days/7)
