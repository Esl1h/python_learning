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


















































