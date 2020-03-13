# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:46:53 2020

@author: esli
"""

from kivy.app import App
from kivy.uix.button import Button

def click():
    print("O botão foi clicado")
# a mensagem virá no console

def build():
    bt = Button(text="clique aqui")
    bt.on_press = click
    return bt

janela = App()
janela.build = build
janela.run()