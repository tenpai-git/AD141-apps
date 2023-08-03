#!/usr/bin/python3

def innerFunction(x,y):
    return x + y

def outerFunction():
    sumNum = innerFunction(g,m)
    print(sumNum)

g = 5
m = 10

outerFunction()
