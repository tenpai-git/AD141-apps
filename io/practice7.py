#!/usr/bin/python3
import sys

def readCommandLine():
    a = []
    for i in range(len(sys.argv)):
        if i > 0:
            a.append(sys.argv[i])
    return a

def main():

    files = readCommandLine()
    if len(files) == 2:
        first_input_filename = files[0] 
        second_input_filename = files[1]
    else:
        print("Two filenames not provided, please provide the files to compare for name comparison.") 
        first_input_filename = input("Enter a file name: ") 
        second_input_filename = input("Enter second filename: ") 
        print("\n")

# Compare lines of each file for a match.
    try:
        with open(first_input_filename, "r") as input_file:
            input_text = input_file.readlines()
            for single_line in input_text:
                with open(second_input_filename, "r") as second_input_file:
                    second_input_text = second_input_file.readlines()
                    for second_line in second_input_text:
                        if second_line == single_line:
                            print("Match Found! ", second_line)
#
    except FileNotFoundError as err:
        print("Invalid input file. This file must exist in this directory already.")

if __name__ == "__main__":
    main()



