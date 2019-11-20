#!/usr/bin/python
from tendo import singleton
import time

me = singleton.SingleInstance()
# tenstando o SingleInstance do lendo, usando sleep para rodar o script em paralelo
time.sleep(10)
