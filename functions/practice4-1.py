#!/usr/bin/python3

def positive_integer():
    prompt = int(input("Please enter a positive integer: "))
    if prompt > 0:
        return prompt
    else:
        return 0

test = positive_integer()

while test == 0: 
    print("Invalid entry, please try again.")
    test = positive_integer()

print("Number is positive!")

