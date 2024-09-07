#!/usr/bin/python3

"""
Exercise 2
Write a program that saves a dictionary as a JSON file.
• The dictionary should contain the word frequency (words as keys, frequency as values) read
from the cyclone file.
• When saving the JSON file, the indentation level should be tab characters.
• The program should display the word that appeared most often in the file.
Sample output:
'the' occurred 93 times
"""

import re
import json

def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key
    return "Key doesn't exist"

def main():

    with open("cyclone", "r") as raw_data:
        filetext = raw_data.read()
        #Select all words.
        regex_test = r"(\b\w+\b)"
        pos_test = re.findall(regex_test, filetext)
        information = {}
        print("File opened successfully.")

        if pos_test:
            print("Regex words found, building frequency dictionary.", end="\n\n")
            #Test each word matched for frequency.
            for element in pos_test:
                frequency = 0
                word = element
                #Increment the value for each word appearing in the list. 
                for value in pos_test:
                    if element == value:
                        #pos_test.remove(value)
                        frequency += 1
                information[word] = frequency 

        else:
            print("Result: No words found in this file.", end="\n\n")

    #Write the data to a tab-level indented file.
    #seps = (',', '\t')
    seps = (',', ': ')
    with open("ex2_output.json", "w") as jfile:
        json.dump(information, jfile, separators=(seps), indent='\t', skipkeys=True, sort_keys=True)
        print("Tab-indented frequency dictionary successfully written to ex2_output.json")
        print()

    #Sort the keys into a list.
    frequency_list = sorted(list(information.values()), reverse=True)

    #Retrieve the highest key. 
    highest_key = get_key(frequency_list[0], information)

    print("The highest key found first was \"{}\" which occured {} times.".format(str(highest_key), str(frequency_list[0]))) 

if __name__ == "__main__": 
    main()

