#!/usr/bin/python
#
# main.py
# Copyright (C) eros 2011 <eros@>
# 
# hora is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# hora is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


#coding: utf-8
#pygtk.require('2.0')
#! /usr/bin/env python
#-*- coding: utf-8 -*-
import pygtk
import gtk
import gobject
minuto = 0

janela = gtk.Window (gtk.WINDOW_TOPLEVEL)	
label  = gtk.Label("Ta na hora de descansar")
janela.add(label)
janela.show_all()

def verificar():
	global minuto
	if (minuto < 30):
		minuto = minuto+1
		janela.hide_all()
	else:
		janela.show_all()
		minuto = 0
	return True	

a = gobject.timeout_add(60000, verificar)

gtk.main()
