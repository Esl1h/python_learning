#!/usr/bin/python3
"""
requirements: 
    pip3 install tendo 
"""
from tendo import singleton
import time

me = singleton.SingleInstance()
# testando o SingleInstance do lendo, usando sleep para rodar o script em paralelo
time.sleep(10)
