#!/bin/python3

prompt = "Enter a name (or the word 'end' to quit): "
verify = set()
while True:
    data = input(prompt)
    if data == "end":
        break
    else:
        #Check for duplicates before adding into the set. 
        verify.update(data.split())

print("The set is: " + str(verify)) 

word_list = list()

for element in verify:
    print(element)
    word_list.append(element)

word_list.sort()
print(word_list)
print("The word list has " + str(len(word_list)) + " unique words total.")
