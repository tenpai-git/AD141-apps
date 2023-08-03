#!/usr/bin/python3

def innerFunction(x,y):
    return x + y

def outerFunction(a,b):
    sumNum = innerFunction(a,b)
    print(sumNum)

g = 5
m = 10

outerFunction(g,m)
