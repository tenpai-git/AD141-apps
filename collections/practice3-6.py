#!/bin/python3

prompt = "Enter a name (or the word 'end' to quit): "
verify = dict()
i = 0
while True:
    data = input(prompt)
    if data == "end":
        break
    else:
        #Update an element and add to dictionary. 
        newdict = dict()
        newdict[i] = data
        verify.update(newdict)
        i = i + 1

print("The dictionary is: " + str(verify)) 
#Sort By Key 
sorted_dict_key = dict(sorted(verify.items()))
#Sort By Value, Inverting
inverted_dict = {v: k for k, v in verify.items()}
sorted_dict_value = dict(sorted(inverted_dict.items()))

print(sorted_dict_key)
print(sorted_dict_value)
