#!/usr/bin/env python
y = int(raw_input("digite um numero :"))
for i in range(11):
	x = lambda i,y:(i*y)
	print "%d X %d = %d" % (y,i,x(i,y))