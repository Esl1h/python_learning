#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:30:02 2020

@author: esli

slides and lessons from  ProgrammingHub course:
    Python Advanced

Attention: Most examples in "Python Advanced" course are wrong. Doesn't work.
Some are syntax erros, others are identation issues.

# https://programminghub.io/coursedetail/23
"""

# create a file
# w = write/writing - irá criar o arquivo, caso já exista, irá apaga-lo totalmente
open('file.txt','w')

saveFile = open('file.txt','w')

# enviar 'texto' para o file.txt
saveFile.write('text: ') 

# enviar conteudo para o file.txt
conteudo = 'Olá isto é uma frase não muito criativa'
saveFile.write(conteudo) 

saveFile.close()


# Adicionando ao arquivo já existente:
# a = Appending

appendFile = open('file.txt','a') 

appendFile.write('mais três palavras')
# somente grava depois de fechar:
appendFile.close()



# variable exemple:
File_var = open('variable.txt','w')
File_var.write('first')
# somente grava depois de fechar:
File_var.close()



# reading
# variavel readMe (criativo né?)
readMe = open('file.txt','r').read()
print(readMe)


""" 
Function open:

    open(‘filename’,’w/a/r’)

w stands for writing to a file
a stands for appending to a file
r ​stands for reading from a file

"""

#write to file 
text = 'Donald trump runs for president' 

#Creates Presidency.txt
saveFile = open('Presidency.txt','w') 

#Writes text to Presidency.txt
saveFile.write(text)

print('File Created : Presidency.txt')  
saveFile.close()

#append from file 
appendME = 'Donald trump is elected president of United states of America' 

#Opens in append mode
appendFile = open('Presidency.txt','a')

#append variable value
appendFile.write(appendME)

# save/close
appendFile.close()




#######################

# OS module

import os

# bash comparison = pwd
os.getcwd()

#return the groupID of current process
os.getgid()

#return the userID
os.getuid()

# return PID
os.getpid()

#create path
os.mkdir('/tmp/test1')

open('/tmp/test1/test.txt','w')


os.makedirs('/tmp/test2')

# remove file
os.remove('/tmp/test1/test.txt') 

# remove recursively
os.removedirs('/tmp/test1')


# rename file or directory:
os.rename('/tmp/test2', '/tmp/test1')

#remove direcory path
os.rmdir('/tmp/test1')





###########################


import os
try:
	# If the file does not exist,
	# then it would throw an IOError
	filename = 'Presidency.txt'
	f = open(filename, 'r')
	text = f.read()
	f.close()

# Control jumps directly to here if
#any of the above lines throws IOError.	

except IOError:

	# print(os.error) will <class 'OSError'>
	print('Problem reading: ' + filename)

	 
# In any case, the code then continues with
# the line after the try/except
    
##############################
    


import os

processId = os.getpid()
userID = os.getuid()
operatingSystem = os.uname()

print(processId)
print(userID)
print(operatingSystem)


##############################
    
"""
 sys module


O módulo sys permite que você use stdin() e stdout(), bem como stderr(), mas, 
mais interessante, podemos utilizar sys.argv().

sys.argv() permite enviar argumentos para o python via command line

"""
import sys

# listar os modulos instalados no python:
sys.builtin_module_names

# versão do python
sys.version


sys.stderr.write('ERROR MESSAGE\n')

sys.stderr.flush()

sys.stdout.write('STDOUT MESSAGE\n')


######### save as test-argv.py
import sys
#for passing arguments
print(sys.argv)

if len(sys.argv) > 1:
	print(sys.argv[1])

######## EOF
    
# Execute com parametro:
# python3 test-argv.py "Hello"



#############################
    
"""
 URLLIB
    
Permite acessar site via python! Download, parse, headers... Requests GET e POST...
urllib no python3 é diferente do urllib2 presente no python2.x

GET - Requests data from a specified resource.
POST - Submits data to be processed to a specified resource.

"""
# urlib = library, request = function of urllib

import urllib.request

x = urllib.request.urlopen('https://www.esli-nux.com/')
print(x.read())





######

import urllib.request 
import urllib.parse 

values = {'q' : 'test'}

data = urllib.parse.urlencode(values)

try: 
	#opens google, ops... bing.com  #and passes test as an argument  
    x = urllib.request.urlopen('https://www.bing.com/search?q=test')
    print(x.read()) 

except Exception as e: 
	#If The request fails the exception is printed 
	print(str(e))  

 
try: 
	url = 'https://www.bing.com/search?q=test'
	#The only values passing now is q=test 
	reqdData = urllib.parse.urlencode(values)  

	# data should be bytes 
	reqdData = data.encode('utf-8')  

	#Requests the page 
	request = urllib.request.Request(url, reqdData) 

	#Gets the response 
	response = urllib.request.urlopen(request) 

	#The Response data is read in readable forms 
	responseData = response.read()
finally:
    sys.stdout.write('STDOUT MESSAGE\n')





#############################
    
"""
 RE = regex, regular expression
 
"""

import re

exampleString = 'Harry is years 11 years old, Lily is 27 years old. James is 32, and his godfather, Sirius is 34'

# get ages
ages = re.findall(r'\d{1,3}',exampleString) 
print(ages)
"""
findall tells Python to return every result found
r is to notify python it is a Regular expression
\d is all integers, which is probably ages
{1,3} means 1-3 counts of digits, or "places"
"""

names = re.findall(r'[A-Z][a-z]*',exampleString)
print(names)


####################################

# Listando as idades e nomes
# criando um dicionário com nome:idade

import re

exampleString = 'Harry is years 11 years old, Lily is 27 years old. James is 32, and his godfather, Sirius is 34'

#r to notify python it is a RE
ages = re.findall(r'\d{1,3}',exampleString)

# * 0 or more repeat
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

x=0

ageDict={}

for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
    
print(ageDict)


##################################3

"""

REGEX PYTHON

IDENTIFIERS:
    \d = any number
    \D = anything but a number
    \s = space
    \S = anything but a space
    \w = any letter
    \W = anything but a letter
    . = any character, except for a new line
    \b = space around whole words
    \. = period. must use backslash, because . normally means any character.
    
MODIFIERS:
    {1,3} = for digits, u expect 1-3 counts of digits, or "places"
    + = match 1 or more
    ? = match 0 or 1 repetitions.
    * = match 0 or MORE repetitions
    $ = matches at the end of string
    ^ = matches start of a string
    | = matches either/or. Example x|y = will match either x or y
    [] = range, or "variance"
    {x} = expect to see this amount of the preceding code.
    {x,y} = expect to see this x-y amounts of the preceding code


WHITE SPACES:
    \n = new line
    \s = space
    \t = tab
    \e = escape
    \f = form feed
    \r = carriage return

[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z


"""
    
################################



import urllib.request
import re

url = 'https://www.w3schools.com/tags/tag_p.asp'

#Requests for url
req = urllib.request.Request(url)

#Response from request
resp = urllib.request.urlopen(req)

#The response data in readable form
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

#print(paragraphs)

for eachP in paragraphs: #Iterating and printing them
	print(eachP)





################################
    
# PYTHON GUI - TKINTER!
    
# TKINTER


# A tiny simple window
class Application:
    def __init__(self, master=None):
        pass
root = Tk()
Application(root)
root.mainloop()


######################


from tkinter import *
class Application:
    def __init__(self, master=None):
          self.widget1 = Frame(master)
          self.widget1.pack()
          self.msg = Label(self.widget1, text="Primeiro widget")
          self.msg.pack ()
root = Tk()
Application(root)
root.mainloop()



######################




from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)
root = Tk()
Application(root)
root.mainloop()









######################
# Another simple window
    
from tkinter import *

class Window(Frame):
#Constructor	
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
 

       
#Creating object
root = Tk() 
app = Window(root)

#Infinite loop
root.mainloop()





########################

# Bottons

from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit")

        # placing the button on my window
        quitButton.place(x=0, y=0)

root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop() 


#########################




from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hello World")
        self.msg.pack ()
        self.bye = Button (self, text="Bye", command=self.quit)
        self.bye.pack ()
        self.pack()
        
app = Application()
app.master.title("Exemplo")
app.master.geometry("200x200+100+100")
mainloop()





###################################


# Threading
import threading
from queue import Queue
import time




##################################



# SQLite3


import sqlite3

# will be created or rewrited
conn = sqlite3.connect('database.db')
c = conn.cursor()

# create a table

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,   keyword TEXT, value REAL)")



def data_entry(): 
	#Inserts values to the table 
	c.execute("INSERT INTO stuffToPlot VALUES(1452549219,\'2016-01-11 13:53:39\',\'Python\',6)") 



create_table()

#call function 
data_entry()


#saves the data 
conn.commit() 


#closes the connection 
c.close() 

conn.close()





##########################







import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db') 
c = conn.cursor() 

def create_table(): 
	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)") 

def data_entry(): 
	c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)") 

def dynamic_data_entry():
     unix = int(time.time()) 
     date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d%H:%M:%S')) 
     keyword = 'Python' 
     value = random.randrange(0,10)
     c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value)VALUES (?, ?, ?, ?)", (unix, date, keyword, value)) 

conn.commit() 
time.sleep(1) 

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')

data = c.fetchall() 
print(data) 

for row in data:	
     print(row) 
c.execute('SELECT * FROM stuffToPlot WHERE value =3')






########################### muah haha

# Logging

import logging

# Types: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='test.log',level=logging.INFO)


logging.basicConfig(filename='test.log',level=logging.INFO,format='%(asctime)s:%(message)s')



###################


# handling


####################
try:
	a+b
except Exception as e:
	print(str(e))

####################
import sys
try:
	 a+b
except:
	#Prints information about the exception that is currently being handled
	print(sys.exc_info()[0])
	print(sys.exc_info()[1])
	print(sys.exc_info()[2].tb_lineno)
 	#Prints error in required format
	print('Error: {}. {}, line:{}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
    

###################


import sys 
import logging
def error_handling(): 
	return 'Error: {}. {}, line:{}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno) 
#This function returns a tuple of three values that give information about the exception that is
#currently being handled

try:
    a+b
except:
   logging.error(error_handling())
   



###################
   
   
# args e kwargs



blog_1 = 'Harry potter is Awesome'
blog_2 = 'Quidditch is my favourite game'
blog_3 = 'You know who, has returned'

def blog_posts(*args):
	for post in args:
		print(post)
blog_posts(blog_1, blog_2, blog_3)



################

