#!/bin/python3

prompt = "Enter a name (or the word 'end' to quit): "
verify = {""}
duplicate_counter = 0 
while True:
    data = input(prompt)
    if data == "end":
        break
    else:
        #Check for duplicates before adding into the set. 
        for element in verify.copy(): #Need to run against a copy!
            #print("Element: " + element + " Data: " + data)
            #If the inputted data is not in the set, add it. 
            if data != element:
                verify.add(data)
            #Otherwise, say it is not unique. 
            else:
                duplicate_counter += 1
                print("Not a Unique Name. Incrementing Counter")

verify.remove("");
print(verify)
print("Duplicates Removed: " + str(duplicate_counter))
