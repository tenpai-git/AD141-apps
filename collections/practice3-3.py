#!/bin/python3

prompt = "Enter a number (or the word 'end' to quit): "
verify = {""}

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
                print("Not a Unique Name")
verify.remove("");
print(verify)
