#!/usr/bin/python3

print("Using list comprehensions, make a list of elements 0-99: ")
print([x for x in range(0,100)])
print("Using list comprenhensions, make the same list but only numbers evenly divisible by 5: ")
print([x for x in range(0,100) if x % 5 == 0])


