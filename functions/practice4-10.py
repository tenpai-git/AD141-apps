#!/usr/bin/python3

def outerFunction(a,b):
    sumNum = (lambda: a + b)()
    return sumNum

g = 5
m = 10

result = outerFunction(g,m)
print(result)
