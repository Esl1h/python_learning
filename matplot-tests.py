#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  12 21:05:31 2020

@author: esl1h
Python3
"""
import matplotlib.pyplot as plt

plt.plot ( [ 1, 2, 3, 4 ] )
plt.ylabel ( 'some numbers' )
plt.show ( )

x = [ 21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100 ]
num_bins = 5
plt.hist ( x, num_bins, facecolor='blue' )
plt.show ( )
