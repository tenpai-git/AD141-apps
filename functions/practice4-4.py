#!/usr/bin/python3

def newSum(*args):
    newList = []
    for element in args:
        newList.append(element)
    return tuple(newList)


print(newSum(5,6,7))
print(type(newSum(5,6,7)))
