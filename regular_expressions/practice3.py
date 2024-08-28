#!/usr/bin/python3

#Examples:
#Sort four character identifier, any white space, and a description
#Sort AA11 Description
#Sort AB22  Description
#Sort AC33             Description
#Don't sort AAAA Description
#Don't sort B111 Description
#Don't sort AA11 - Description
#For each item print as:

#AA
#11
#Description

#BB
#22
#Description

#!/usr/bin/python3

import re

def print_details(x):
    for y, a_group in enumerate(x.groups(), 1):
        print(a_group)

def main():

    #Read in the data line-by-line
    with open("3_data.txt", "r") as raw_data:
        for data_line in raw_data:
            
            print("Scanning: ", data_line, end="")
            
            #Match any positive or negative number but not any non-digits.
            regex_test = "(^\d\d)([A-Z][A-Z])\s+([a-zA-Z]+)"
            pos_test = re.search(regex_test, data_line)

            if pos_test:
                print("Result: Positive Test", end="\n\n")
                print_details(pos_test)
                print()
            else:
                print("Result: Negative Test", end="\n\n")

if __name__ == "__main__": 
    main()


