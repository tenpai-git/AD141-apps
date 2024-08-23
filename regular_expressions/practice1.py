#!/usr/bin/python3

import re

def main():

    #Read in the data line-by-line
    with open("1_data.txt", "r") as raw_data:
        for data_line in raw_data:
            
            print("Scanning: ", data_line, end="")
            
            #Match any positive or negative number but not any non-digits.
            regex_neg_num = "^(-)+[0-9]+[^0-9]*$"
            regex_pos_num = "^[0-9]+[^0-9]*$"
            pos_test = re.search(regex_pos_num, data_line)
            neg_test = re.search(regex_neg_num, data_line)

            if pos_test:
                print("Result: Positive", end="\n\n")
            elif neg_test:
                print("Result: Negative", end="\n\n")
            else:
                print("Not a pos/negative integer", end="\n\n")

if __name__ == "__main__": 
    main()
