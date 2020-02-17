#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:58:45 2020

@author: esli
"""
import functions

###########################

import math

e = math.e
pi = math.pi

print(e)
print(pi)

###########################

from math import pi, e
print(pi)
print(e)


from math import sqrt
print(sqrt(16))


###########################

def func():
    from math import factorial
    print(factorial(10))

func()


###########################



try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")



###########################














