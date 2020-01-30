#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:06:50 2020

@author: esli
"""

x = 0
while(x <= 10):
    print(x)
    x += 1
else:
    print("stop")


for num in "123456789":
    print(num)


list(range(10))
list(range(0,10))
list(range(0,10,2))
list(range(10,0,-2))
list(range(-10,0,2))

for i in range(10):
    print(i)


for item in range(10):
    print(item)
    if(item==6):
        break
 

print()
print("inicio")
i = 0
while (i < 10):
    i += 1
    if (i%2 == 0):
        continue
    print(i)
else:
    print("else")
print("fim")
print()




print()
print("inicio")
i = 0
while (i < 10):
    i += 1
    if (i%2 == 0):
        continue
    if (i > 5):
        break
    print(i)
else:
    print("else")
print("fim")
print()