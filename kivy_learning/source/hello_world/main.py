# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:21:53 2020

@author: esli
"""

from kivy.app import App
from kivy.uix.label import Label


#App().run()

def build():
    return Label(text = "Hello World")


hello_world = App()
hello_world.build = build
hello_world.run()
