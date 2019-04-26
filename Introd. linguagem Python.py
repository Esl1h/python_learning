# -*- coding: utf-8 -*-
"""
Created on Sun May  8 22:26:07 2016

@author: esl1h
"""

#Operadores (diretamente no terminal python):
2 * 3

10 / 2

5 - 3

4 + 5

3 ** 2

25 % 4 (para retornar o resto)




# variaveis
variavel = 'value'


# print (saída)
print 'Hello World'

# raw (entrada/captura)
var_name = raw_input("What is your name? ")
print var_name

var_num = input("What is your name? ")
print var_num


# Alterando valores de variaveis
valor1=3
print valor1
valor1=5**2
print valor1

# Tipos variaveis
var1 = 10 #valor inteiro / int
var2 = 15.99 # valor de ponto flutuante / float     --> uso de ponto, casa decimal
var3 = True #valor booleano / bool 
var0 = 4+6j #valor complexo / complex               --> uso de operadores

# Descobrir tipo de variavel = type
# print type(variavel)
# exemplo:
print type(var2)


>>> var0 = 4+6j
>>> var1 = 10 
>>> var3 = True
>>> var2 = 15.99

>>> print type(var0)
<type 'complex'>

>>> print type(var1)
<type 'int'>

>>> print type(var2)
<type 'float'>

>>> print type(var3)
<type 'bool'>


# Operação com ponto flutuante e variavel:
>>> var1 / 2.5
4.0

>>> var1/3.5
2.857142857142857

# Tratamento de Strings:

\n #quebra de linha
\t #tabulação
"""  """ (conteudo dentro de 3 aspas duplas) - #uso de multiplas linhas para a string

var9 = """ Teste \n com tratamento \t de strings
usando  aspas
triplas """

>>> print var9
 Teste 
 com tratamento 	 de strings
usando  aspas
triplas

#Requisitando o valor de uma posição na string
                    0 1 2 3
variavel var12 -->  e s l i

>>> var12 = 'esli'
>>> type (var12)
<type 'str'>
>>> var12[2]
'l'

>>> var12[0]
'e'

>>> var12[0:2]
'es'

>>> var12[0:3]
'esl'

>>> var12[0:4]
'esli'

>>> var12[1:4]
'sli'

>>> var12[2:4]
'li'




# Operadores com strings:

>>> var20 = 'primeiro'

>>> print var20 * 2
primeiroprimeiro

>>> print var20 + 'teste'
primeiroteste


# Operadores Condicionais (retorna True ou False)

#Igualdade
==

#Diferença
!=

#menor que
<

#maior que 
>

#maior ou igual
>=

#menor ou igual
<=


#Agrupar condicionais

#e
and

#ou
or

#não
not

Exemplo (executa a operação e retonra apenas False or True): 
(7 == (2*3.5)and(False or True))





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

#Exibir uma posição na lista
print (c[0])

# alterar o valor de uma posição na lista
b [3] = 50

# Exibir a lista
print(b)

# Exibir o tamanho da lista
print (len(b))

# Adicionar UM elemento no fim da lista
b.append(60)
print (b)
#
# Adicionando varios elementos no fim da lista
b.extend([70,80,90])
print (b)
#
# Adicionando varios itens na lista em posição definida
b.insert(1,15)
print (b)
