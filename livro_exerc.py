#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 22:22:31 2016

@author: esl1h
"""
import math
import sys
sys.version

var1 = (7 == (2*3.5)and(False or True))
print (var1)


print ("Hello World")

number = int(input("insira um numero: "))
print ("o numero e",number)


print ("")
print ("")

print ("Soma de 2 numeros!")
n1=int(input("insira o primeiro numero da soma: "))
n2=int(input("insira o segundo numero da soma: "))
print(n1+n2)

print ("")
print ("")

print ("media de 4!")
nb1=int(input("insira a primeira nota: "))
nb2=int(input("insira a segunda nota: "))
nb3=int(input("insira a terceira nota: "))
nb4=int(input("insira a quarta nota: "))
print ("A media e:",((nb1+nb2+nb3+nb4)/4))

print ("")
print ("")



b=28
a=(b*2)
c= a-b
print (a)
print (c)



num = int(input("Digite um valor:"))
if num>10:
   print ("Numero maior que 10")
else:
   print ("Numero menor que 10")




num = int(input("Digite um valor:"))
if num == 0:
	print ("O numero e zero")
elif num > 0:
   print ("Numero positivo")
else:
   print ("Numero negativo")
   
   
   
   
   
# MEDIA
print ("media de 4!")
nb1=int(input("insira a primeira nota: "))
nb2=int(input("insira a segunda nota: "))
nb3=int(input("insira a terceira nota: "))
nb4=int(input("insira a quarta nota: "))
media = (nb1+nb2+nb3+nb4)/4
print ("Você está:")
if media >= 7:
    print ("Aprovado", media)
elif media <= 5:
    print ("Reprovado", media)
else:
    print("Recuperaçao", media)
    

# WHILE
opc=1
while opc == 1:
    num = int(input("Digite um valor:"))
    if num == 0:
    	print ("O numero e zero")
    elif num > 0:
       print ("Numero positivo")
    else:
       print ("Numero negativo")
    resp = input("Deseja finalizar? (s/n)")
    if resp != "n":
        opc = 0
print ("Algoritmo finalizado")


# WHILE
opc=1
while opc == 1:
    num = int(input("Digite um valor:"))
    if num % 5 == 0:
    	print ("O numero e divisivel por 5")
    else:
       print ("O numero não e divisivel por 5")
    resp = input("Deseja finalizar? (s/n)")
    if resp != "n":
        opc = 0
print ("Algoritmo finalizado")



# FOR
frase = "Isto e um teste"
for letra in frase:
    print (letra)
    
    
# Range
list(range(0,10))
list(range(0,10,3))


# Range + FOR
maiornota = 0
for cont in list(range(10)):
    nota = int(input("Digite a nota:"))
    if nota > maiornota:
        maiornota = nota
print ("A maior nota é:",maiornota)



# Listas
a=[]
b=[10,20,30,40]
c=[40,4.5,"sr"]
print (c[0])
b [3] = 50
print(b)


