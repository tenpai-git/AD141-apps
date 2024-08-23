#!/usr/bin/python3

import re

def main():

    #Read in the data line-by-line
    with open("2_data.txt", "r") as raw_data:
        for data_line in raw_data:
            
            print("Scanning: ", data_line, end="")
            
            #Match any positive or negative number but not any non-digits.
            regex_float_neg_num = "^(-)+[0-9]+\.[0-9]+[^0-9]*$"
            regex_float_pos_num = "^[0-9]+\.[0-9]+[^0-9]*$"
            pos_test = re.search(regex_float_pos_num, data_line)
            neg_test = re.search(regex_float_neg_num, data_line)

            if pos_test:
                print("Result: Positive Float", end="\n\n")
            elif neg_test:
                print("Result: Negative Float", end="\n\n")
            else:
                print("Not a pos/negative float", end="\n\n")

if __name__ == "__main__": 
    main()
