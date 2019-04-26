#!/usr/bin/python

import pygtk
import gtk

pygtk.require('2.0') #recomento que esteja instalada essa vercao

class j_princ: #criamos a classe da janela
   
   def __init__(self): #definimos a funcao principal
      self.janela = gtk.Window() #definimos a janela
      self.janela.set_title("Minha Janela") #damos um titulo
      self.janela.set_border_width(15) #definimos a largura da borda
      self.janela.connect('destroy', self.fechar, self.janela) #e criamos o envento de sair
      
      self.conteudo = gtk.VBox(False, 1) #criamos um VBox e dois HBox
      self.msgBox = gtk.HBox(False, 2)
      self.boxButton = gtk.HBox(False, 1)
      
      self.msgBox.set_border_width(8) #definimos a borda dos HBox
      self.boxButton.set_border_width(8)
      
      self.rotulo1 = gtk.Label("Digite a mensagem a ser enviada:") #criamos um rotulo, para nao tem que ser impresso no terminal
      self.mensagem = gtk.Entry() #criamos a caixa de texto
      self.btnEnviar = gtk.Button("Enviar") #criamos o botao
      self.btnEnviar.connect('clicked', self.ev_Enviar, self.mensagem) #criamos um envento para o mesmo
      self.btnSair = gtk.Button("Sair") #criamos outro botao
      self.btnSair.connect('clicked', lambda w: self.janela.destroy()) #criamos o evento usando 'lambda W'
      
      self.conteudo.pack_start(self.rotulo1, False, False, 0) #inserimos os componentes no Boxs
      self.msgBox.pack_start(self.mensagem, False, False, 0)
      self.conteudo.pack_start(self.msgBox, False, False, 0)
      self.boxButton.pack_end(self.btnSair, False, False, 0)
      self.boxButton.pack_end(self.btnEnviar, False, False, 0)

      self.conteudo.pack_start(self.boxButton, False, False, 0)
      
      self.janela.add(self.conteudo) #inserimos o box pricipal na janela
   
   def fechar(self, widget, window): #evento sair
      window.hide() #minimisa a janela
      gtk.main_quit() #finaliza o loop da gtk
      print "\n\n" #imprime dois enters
   
   def ev_Enviar(self, widget, entry): #evento enviar
      self.texto = entry.get_text() #busca o texto da entry
      print "\n\n", self.texto #imprime na tela dois enters e o texto da entry
   
   def show(self): #criamos o evento de carregar a janela
      self.janela.show_all() #carrega a janela e todos os componentes dentro dela

princ = j_princ() #determinamos a variavel na janela

if __name__ == "__main__":
   princ.show() #iniciamos a janela
   gtk.main() #iniciamos o loop gtk
