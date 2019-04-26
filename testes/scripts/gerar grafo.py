#!/usr/bin/env python

#gerador de grafos orientados v1.0
#autor: Xerxes Lins (xerxeslins@gmail.com)
#voce precisa ter o graphviz instalado para que funcione
#no Slackware -> slapt-get --install graphviz
#tbm é recomendado o visualizador de imagens gqview

import os

arquivo = open('grafo.txt','w')
arquivo.write('digraph G {\n')
print
print 'Ajuda: responda o que se pede e use -- (dois tracos) para encerrar'
print
vp = raw_input('Digite um vertice: ')
while vp != '--':
   msg = 'Digite um vertice adjacente ao vertice %s: ' % vp
   vs = raw_input(msg)
   if vs != '--':
      msg = 'Digite o nome da aresta que liga o vertice %s ao vertice %s: ' % (vp, vs)
      aresta = raw_input(msg)
      if len(aresta) == 0:
         msg = '%s -> %s\n'  % (vp, vs)
      else:
         msg = '%s -> %s [ label=%s ];\n'  % (vp, vs, aresta)
      print
      arquivo.write(msg)
   vp = raw_input('Digite um vertice: ')
   vs = '0'   
arquivo.write('}')
arquivo.close()
os.system('dot -Tgif grafo.txt -o grafo.gif')
os.system('gqview grafo.gif')
