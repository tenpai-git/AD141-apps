#!/bin/python3

#Concatenate lists.
first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
result = []

for element, prefix in enumerate(first):
    result.append(prefix + second[element])
print(result)
