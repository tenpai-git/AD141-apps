#!/usr/bin/python3

def valueAdd(dictionaryVal, number):
    new_dict = dict()
    for key, value in dictionaryVal.items():
        value += number
        new_dict[key] = value
    return new_dict

dictionaryValues = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
adder = 5

print(valueAdd(dictionaryValues, adder))
