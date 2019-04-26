#!/usr/bin/env python

import os
import sys
import pygtk
import gtk

class power:
	
	def restart(self, event):
   	 	command = "sudo shutdown -r now"
   	 	os.system(command)
		
	def shutdown(self, event):
		command = "sudo shutdown -h now"
		os.system(command)

	def SessionEnd(self, event):
		command = "gnome-session-quit --logout"
		os.system(command)
		
	def SessionBlock(self, event):
		command = "gnome-screensaver-command -l"
		os.system(command)

	def cancel(self, event):
		import sys
		sys.exit()
		
	def delete_event(self, widget, event, data=None):
        	gtk.main_quit()
        	return False
	
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Power Botton for GNU/Linux KDu")
		self.window.connect("delete_event", self.delete_event)
		self.window.set_border_width(10)
		
		self.box1 = gtk.HBox(False, 0)
        	self.window.add(self.box1)
	
		self.button1 = gtk.Button("Reiniciar")
		self.button1.connect("clicked", self.restart)
		self.box1.pack_start(self.button1, True, True, 0)
		
		self.button2 = gtk.Button("Desligar")
		self.button2.connect("clicked", self.shutdown)
		self.box1.pack_start(self.button2, True, True, 0)

		self.button3 = gtk.Button("Finalizar Sessao")
		self.button3.connect("clicked", self.SessionEnd)
		self.box1.pack_start(self.button3, True, True, 0)

		self.button4 = gtk.Button("Bloqueia a Sessao")
		self.button4.connect("clicked", self.SessionBlock)
		self.box1.pack_start(self.button4, True, True, 0)
		
		self.button5 = gtk.Button("Cancelar")
		self.button5.connect("clicked", self.cancel)
		self.box1.pack_start(self.button5, True, True, 0)
		
                self.window.set_position(gtk.WIN_POS_CENTER)
		self.button1.show()
		self.button2.show()
		self.button3.show()
		self.button4.show()
		self.button5.show()
		self.box1.show()
		self.window.show()
def main():
	gtk.main()
	
if __name__=="__main__":
	pwr = power()
	main()
