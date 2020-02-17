#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:57:38 2020

@author: esli
"""

# Listas
list = [2, 6, 12 ,0, 32, 4, 8]
type(list)
list[4]
list[5]+list[2]

list1 = ['a', 'b', 'c', 'd', 'e']
list1
list1[0]
list1[3]

list2 = ['a', 4]

##########

list4 = [['a','b','c'], [1,2,3,4],[]]
list4[1]
list4[0]
list4[2]

list4[0][1]

len(list4)

list4[len(list4)-2]

list4[-1]


##########

list5 = [1,2,3,4,5]
list5
list5 = list5 + [6]
list5
list5 = [0] + list5
list5
list5 = list5 + [7,8,9,10]
list5

list5.append(11)
list5

list5.append([11])

del(list5[-1])
list5

lis = 10*[0]
lis


##########


lista_nums = [100,200,300,400]
for item in lista_nums:
    print(item)
    
    
    
lista_nums = [100,200,300,400]
lista_indice = [0,1,2,3]
for item in lista_indice:
    lista_nums[item] += 1000
print(lista_nums)
        
    
lista_nums = [100,200,300,400]
for item in range(4):
    lista_nums[item] += 1000
print(lista_nums)
        
    
lista_nums = [100,200,300,400,500,600]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)
                

lista_nums = [100,200,300,400,500,600]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)
            


##########

lista = "python"
lista[2]
lista[:2]
lista[2:]
lista[::2]
lista[::-1]


list = ['aaa', 'bbb', 'ddd']
list
list[1]

list.append('eee')
list
list.insert(2, 'ccc')
list
list[1] = 'bbbbb'


list.pop()
list
list.pop(0)
list
list.pop(-1)

list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

del(list[2:4])
list

list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
del(list[::2])
list


##########


list_names = ['John','Paul','Ringo','George', 'Ozzy', 'Bill', 'Geezer', 'Tony']

list_names.reverse()
list_names

list_names.sort()
list_names

list_names.sort(reverse=True)
list_names


len(list_names)
list_names[7]
list_names[len(list_names)-1]

list_names

list_names.insert(5, 'John')
list_names

list_names.append('John')
list_names

list_names.count('John')
list_names


list_names.index('Ozzy')
list_names

list_names.index('John')
list_names



############

# tuple

t = 'aaa', 1, True
t
type(t)


# IN
"""
x in [...] # to list
x in (...) # to tuple
x in {...} # to dictionary

"""

1 in t
2 in t
3 not in t

if 1 in t:
    print("contido")
else:
    print("não contido")



###########



a = 10
b = 25
c = 66

x = int(input("Digite um numero: "))
if(x == a or x == b or x == c):
    print("Está contido")
else:
    print("Não está contido.")


x = int(input("Digite um numero: "))
if(x in [a,b,c]):
    print("Está contido")
else:
    print("Não está contido.")



###########


cores = ["azul", "branco", "vermelho", "roxo", "preto"]

while True:
    cor = input("Digite o nome de uma cor ou "
                "'0' para sair do programa: ")

    if (cor=="0"):
        break
    elif cor in cores:
        print("Esta cor está contida na lista")
    else:
        print("Esta cor não está contida na lista")
    print()



























