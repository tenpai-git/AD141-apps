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
        input_filename = files[0] 
        output_filename = files[1]
    else:
        print("Alright this is fundamentally just a simple copy program in Python.") 
        input_filename = input("Enter a file name: ") 
        output_filename = input("Enter output filename: ") 
        print("\n")

# Read the input file with .readline()
    try:
        with open(input_filename, "r") as input_file:
            input_text = input_file.readline()
            print("Read input file: ", input_text)

    # Write to the output file with .write()

        with open(output_filename, "w") as output_file:
            output_file.write(input_text)
            print("Written to output file: ", output_filename)

    except FileNotFoundError as err:
        print("Invalid input file. This file must exist in this directory already.")

    except OSError as oserr:
        print("Unable to open file! There may be a permissions issue. Exiting this program."

if __name__ == "__main__":
    main()



