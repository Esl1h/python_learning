#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:52:02 2020

@author: esli

slides and lessons from  ProgrammingHub course:
    Python
    Python 3
"""

# https://programminghub.io/coursedetail/6 
# https://programminghub.io/coursedetail/62

print("Hello World!... again!")

# Strings:
MYVAR1 = "Hello"
MYVAR2 = '451'
MYVAR3 = "45Number"


# Numbers are floating point, integer:
MYVAR4 = 2       # An Integer
MYVAR5 = 25.54   # A floating point number


# Giving input to a program
MYVAR6 = input('Enter a number: ') # this is not a number, it is a string!
print(MYVAR6)

"""
    >
    <
    <>
    ==
    >=
    !=
    %
    
    logical: AND, OR, NOT
"""

num1 = int(input("Enter First number: "))	# taking input for first number  
num2 = int(input("Enter Second number: "))	# taking input for second number 
sum = num1 + num2	# adding num1 and num2 and storing them in sum 
print(sum)	# print sum to the screen

"""
Decisions:
    if
    if-else
    if-elif
    
Use a colon : to separate the different parts of expression, like:
    if condition:
         statements if true
"""         



if 5 == 5:
	print("You successfully learned if statement.")

if 5 > 9:
	 print("Oops! Not this time.")




"""       
    if condition:
        statements if true
    else:
        statements if false
"""

if 5 == 3:
	print("You successfully learned if statement.")
else:
	print("Wow! You also learned about else statement.")


"""
    if condition1:
    	statements 
    elif condition2:
    	statements 
    elif condition3:
    	statements 
    else:
    	statements

"""

if 5==4:
	print("An if statement. Oh!")
elif 4==4:
	print("That’s something new.")
elif 4>=9:
	print("Really?")
else:
	print("Not this time")




"""
Loops:
    For
    While
    
"""

for num in range (1,101):
    print(num)


for num in range (0,10,2):
    print(num)

for num in range (1,10,2):
    print(num)



"""
 while condition:
	statements
"""

num = 0
while (num < 10):
	print(num)
	num = num + 1	#update the value of num by 1




"""
Functions:
    
    def functionName (parameters):
        tements
        return something

 functionName(parameters)

"""

def addNumbers(num1, num2):
	sum = num1 + num2
	return sum

# Anothers examples:
def helloWorld():	# Define the helloWorld function.
	print("Hello World")
"""
"""
helloWorld()	# Call to helloWorld function.


def addNumber(num1, num2):
	sum = num1 + num2
	print(sum)
	return 
addNumbers(2,3) 
addNumbers(4,5)


def subtract(a,b):
	diff = a-b
	print(diff)

subtract(9,4)


#####################

# Math module

import math
 # to use a function of math module, use: math.functionName()
 
import math 
math.pow(4,3) #exponention 


import math 
a = math.floor(4.3)  
b = math.floor(10.9)  
print (a) 
print (b)
# math.floor returns the largest integer equal to or less than the number passed as the parameter


import math 
a = math.ceil(4.3)  
b = math.ceil(10.9)  
print (a) 
print (b)
# math.ceil  returns the smallest integer equal to or greater than the number passed as the parameter


import math 
a = math.log(10)  
b = math.log(10,2)  
print (a) 
print (b)
# o módulo matemático fornece uma função para encontrar o logaritmo do número também. math.log () pode receber um ou dois parâmetros. Quando um parâmetro é passado, ele retorna o logaritmo natural desse número. Quando dois parâmetros são passados, ele retorna o logaritmo do primeiro número para a base do segundo número.


import math 
a = math.sqrt(9)  
b = math.sqrt(16)  
print (a) 
print (b)






a = abs(10)  
b = abs(-10)  
print (a) 
print (b)
# abs return an absolute value, An absolute value is the magnitude of number irrespective of its sign



#####################

# Strings

str = "Here I am"

str.capitalize()
str.count("e")
str.count("Am")
str.count("am")

a = str.find("r") 
print (a)
# the 'r' are 2º position (0,1,2... "heRe I am")


str = " " 
iter = ("I","am","awesome.") 
a = str.join(iter)  # A str.join() function returns the concatenated string of the sequence of strings passed to it.
print(a)


str = "-" 
iter = ("I","am","awesome.") 
a = str.join(iter) 
print(a)



#####################

# Lists
list1 = [2, 4, 5, 6, 7, 2]
list2 = [4, "hi", 6, "Me", 78]

list1[1]

print(list1[1]) # print the index number 1 from a list, "4" in this example.
 
list1 = [2, 4, 5, 6, 7, 2] 
a = list1[1:4] 
print(a) 

list1 = [2, 4, 5, 6, 7, 2] 
list1[:]

list1[:5]
list1[2:]


# change value on list
list2 = [4, 55, 6, 7, 8, 9, 90]
list2[4] = 88 #change 4rd item from '8' to '88'
print(list2[:])

# add value to list
list2.append(150)
print(list2[:])

# delete item, 4rd on a list, '88' value:
del list2[4]
print(list2[:])

# remove a value (not a position index):
list1 = [4, 5, 6, 2 ,1]  
list1.remove(5) 
print(list1)



#####################

# tupla
tuple1 = (2, 4, 5, 6, 7, 2)
tuple2 = (4, "hi", 6, "Me", 78)

tuple1[1]
print(tuple1[1])

tuple1[1:4]
print(tuple1[1:4])

del tuple1
# tuple cant be updated or removed



#####################

# Dictionary = key + value

dict1 = {
	'name'  : 'xyz',
	'age'   : 25,
	'hobby' : 'Dancing'
}


dict1['age']
print(dict1['age'])
print(dict1['name'])

print(dict1)


# update:
dict1['name'] = 'abc'

# add new key:
dict1['profession'] = 'pilot'

# delete key or all dictionary:
del dict1['name']

# keep a dict, but remove all keys and values:
dict1.clear()

del dict1



