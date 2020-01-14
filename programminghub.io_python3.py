#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:52:02 2020

@author: esli

slides and lessons from  ProgrammingHub course:
    Python 3
"""

# Python:
# https://programminghub.io/coursedetail/6 

# Python3:
# https://programminghub.io/coursedetail/62

# Only some differences between this courses

print("Hello World!... again!")


# Walrus-operator :=

# it is a way to assign to variables within an expression using the notation NAME := expression

# For example,
#using assignment operator 
variable=False 
print(variable) 

# Assignment expressions allow you to assign and return a value in the same expression. For example, if you want to assign to a variable and print its value:
#using Walrus operator 
print(variable := False)




#############

# Lambda functions

# also known as anonymous functions, are small, restricted functions which do not need a name
# lambda expressions (or lambda forms) are utilized to construct anonymous functions
adder = lambda x, y: x + y
print (adder (1, 2))

"""
Here, we define a variable that will hold the result returned by the lambda function.
The lambda keyword used to define an anonymous function.
x and y are the parameters that we pass to the lambda function.
This is the body of the function, which adds the 2 parameters we passed. Notice that it is a single expression. You cannot write multiple statements in the body of a lambda function.
We call the function and print the returned value.

"""
# without lambda funtion:

def add(x ,y):
	num3= x + y
	return num3

print (add (1, 2))



#############

# math

# math.fabs

a = math.fabs(10)  
b = math.fabs(-10)  
print (a) 
print (b)
# math.fabs return an absolute value, An absolute value is the magnitude of number irrespective of its sign
# like "abs" function
