# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:46:53 2020

@author: esli
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

def click():
    print(ed.text)

def build():

    layout = FloatLayout()

    global ed
    ed = TextInput(text="Texto!")
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button(text="Clique aqui")
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.x = 170
    bt.y = 150
    bt.on_press = click


    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout


janela = App()
janela.title = "Text to terminal console"

from kivy.core.window import Window
Window.size = 500,650

janela.build = build
janela.run()