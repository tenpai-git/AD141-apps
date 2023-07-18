#!/bin/python3

digit_dict = { "Zero":0,"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10 }

prompt = input("Input a set of integers to convert into words.") 
text = "{}, "
output = str()

#Reverse lookup dictionary for Key. 
for integer in prompt:
    for key, value in digit_dict.items():
        if int(integer) == int(value):
            output += text.format(key)

print(output[:-2])
