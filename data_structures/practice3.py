#!/usr/bin/python3

from math import factorial

lister = {x:factorial(6*x)*factorial(5*x) for x in range(1,10)}
print(lister)

