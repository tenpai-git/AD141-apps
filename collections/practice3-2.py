#!/bin/python3

prompt = "Enter a number (or the word 'end' to quit) "
numbers = []
while True:
    data = input(prompt)
    if data == "end":
        break
    else:
        numbers.append(int(data))

print("Your list of numbers is: " + str(numbers))

summation = 0
for element in numbers:
    summation += element

print("The sum of your numbers is: " + str(summation))

