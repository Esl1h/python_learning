# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:46:53 2020

@author: esli
"""

from kivy.app import App
from kivy.uix.label import Label

def build():
    #return Label(text="Hi! I'm a text", italic=True, font_size=50)
    lb = Label()
    lb.text="Hi! I'm a text"
    lb.italic=True
    lb.font_size=50
    return lb

app = App()
app.build = build
app.run()