#!/usr/bin/python3

def compare(mass_input, number):
    compare_counter = int(0)
    number = int(number)
    for element in mass_input:
        if element > number:
            compare_counter += 1
    return compare_counter
    
newList = []

print("This program will compare a list of numbers against a secondary input and check all the arguments for which is bigger, the list element or the secondary input, and return the number of occurences of this behavior.")

while True:
    prompt = input("Enter a number into the list. Type \"next\" to move to the secondary input (end to exit): ") 

    if prompt == "next":
        second = input("What number will the list elements compare against?: ")
        output = compare(newList, number=second) #Must be followed by keyword because first takes multiple arguments.
        break

    if prompt == "end":
        break

    else:
        newList.append(int(prompt))

print(output)
