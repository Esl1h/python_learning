#!/usr/bin/python3

import sys
no = ' '
fd = open('teste.tmp','w')
old_stdout = sys.stdout
sys.stdout = fd
# Agora todas vão para o arquivo teste.tmp
print("teste")

largura = 2
comprimento = 7
print('A largura e', largura)
print('O comprimento e', comprimento)
print('A area e', (largura * comprimento))
print('O perimetro e', (largura * 2 + comprimento * 2))


#aqui as msgm voltam para o console
sys.stdout = old_stdout


#fechar o arquivo:
fd.close()


#import sys  # Need to have acces to sys.stdout
#fd = open('foo.txt','w') # open the result file in write mode
#old_stdout = sys.stdout   # store the default system handler to be able to restore it
#sys.stdout = fd # Now your file is used by print as destination 
#print 'bar' # 'bar' is added to your file
#sys.stdout=old_stdout # here we restore the default behavior
#print 'foorbar' # this is printed on the console
#fd.close() # to not forget to close your file
