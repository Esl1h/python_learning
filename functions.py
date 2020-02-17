#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:28:09 2020

@author: esli
"""

# Functions:

def hello():
    print("Hello World!")

hello()

###########

def soma(x, y):
    total = x+y
    print("soma: ", total)

soma(10, 50)


###########

def login(user="root", passwd="toor"):
    print("User: ", user)
    print("pswd: ", passwd)


login()
login("john","123")

###########


def dados(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))
    
dados("John", "Paul Jones", 61, True)

dados(nome="Jimmy",  sobrenome="Page", idade=65, sexo=True)



##########


def func():
    return 1, 2

a, b = func()

print(a)
print(b)



##########

def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado, cubo

q,c = potencia(10)

print(q)
print(c)


##########

# args
def argumentos_list(*lista):
    print(lista)
    
argumentos_list(1,2,3,4,5,6)
argumentos_list("um", "dois", "tres", "quatro")



##########

# kwargs
def argumentos_dict(**dicionario):
    print(dicionario)

argumentos_dict(um=1, dois=2, tres=3, quatro=4)
argumentos_dict(a=1, b=2, c=3, d=4)


###########



def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)
    
argumentos(1,2,3,4, um=1, dois=2, tres=3, quatro=4)


##########



def func():
    print("func")
    
    def func_interna():
        print("func_interna")
        
    func_interna()
    
func()


###########

# NONLOCAL / GLOBAL

def func():
    var_local = 10
    
    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)
    
    func_interna()
    
func()




x = 10

def funcX():
    global x
    return x

print(funcX())



#########


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número inválido.")


num1 = input_float ("Digite o primeiro número: ")
num2 = input_float ("Digite o segundo número: ")

try:
    print (num1 / num2)
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")













