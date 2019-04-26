#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Faça um programa que receba dez números e que calcule e mostre
#a quantidade de números entre 30 e 90
a = [] #lita vazia
contador = 0 
for cont in range(10): #Pede 10 números ao usuário
    a.append(eval(input("Número: "))) #coloca os números na lista a
for i in a:
    while 30<i<90: #enquanto o i valer entre 30 e 90 somar 1 a variavel contador
        contador = contador + 1
        break
print("A quantidade de números entre 30 e 90 é: %d" % contador) 
    
