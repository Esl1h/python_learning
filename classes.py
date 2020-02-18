#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:58:45 2020

@author: esli
"""


class Estudo1():
    pass


p1 = Estudo1()
p2 = Estudo1()

print(id(p1))
print(id(p2))


######################



class Retangulo:
    
    def __init__(self):
        self.a = 0
        self.l = 0
    
    def area(self):
        return self.a * self.l
        
        
        
r1 = Retangulo()
r2 = Retangulo()

r1.l = 10
r1.a = 5

print(r1.area())



######################




class Retangulo2:
    
    def __init__(self, largura, altura):
        self.a = altura
        self.l = largura
    
    def area(self):
        return self.a * self.l



r3 = Retangulo2(7, 5)
print(r3.area())


######################


# GET e SET



class Retangulo3:
    
    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)
    
    def set_altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura invalida: {}".format(num))
        self.altura = num
        
    def set_largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("largura invalida: {}".format(num))
        self.largura = num
        
        
    def get_area(self):
        return self.altura * self.largura
        



r4 = Retangulo3(largura=10, altura=5)
print(r4.get_area())



######################




class Retangulo5:
    
    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.set_altura(altura)
        self.set_largura(largura)
    
    def set_altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura invalida: {}".format(num))
        self._altura = num
        
    def set_largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("largura invalida: {}".format(num))
        self._largura = num
        
        
    def get_area(self):
        return self._altura * self._largura
        

r5 = Retangulo5(largura=10, altura=5)
print(r5.get_area())



######################

