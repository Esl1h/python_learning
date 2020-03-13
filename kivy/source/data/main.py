# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:46:53 2020

@author: esli
"""

from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text="Componente TextInput")


janela = App()
janela.build = build
janela.run()