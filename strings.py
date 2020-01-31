#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:24:29 2020

@author: esli
"""

s = "This is a Python string"
print(s)

s[0]
type(s[0])

s[-1]
s[0:9]
s[::2]
s[12:]
s[:12]
s[10:16]
s[::-1]
s[::-2]


##########

chr(100)
ord("a")
'''

>>> for c in range(123):
    str(c) + " - " + chr(c)

'''


len(s)
print(s)
s[3]

s.split(" ")

lista = s.split(" ")
lista[0]+" "+lista[3]

s.replace("This", "  ")



##########


for c in s:
    print(c)


indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice += 1

for k, v in enumerate(s):
    print(k, v)

dict(enumerate("This is a Python string"))



##########

# dicts:

d1 = {}
type(d1)


d1 ['aaa'] = 1000
d1 ['bbb'] = 2000
d1 ['ccc'] = 3000
d1 ['ddd'] = 4000

print(d1)

d1['bbb']


d2 = {1.1: "teste1", 2.2: "teste2", 3: "teste3"}
d2[1.1]
d2[2.2]














