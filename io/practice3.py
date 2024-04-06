#!/usr/bin/python3

def main():
    
# Ask the user for the name of the input file.
    print("Alright this is fundamentally just a simple copy program in Python.") 
    input_filename = input("Enter a file name: ") 
    output_filename = input("Enter output filename: ") 

# Ask the user for the name of the ouput file.

# Read the input file with .readline()
    try:
        with open(input_filename, "r") as input_file:
            input_text = input_file.readline()

    # Write to the output file with .write()

        with open(output_filename, "w") as output_file:
            output_file.write(input_text)

    except FileNotFoundError as err:
        print("Invalid input file. This file must exist in this directory already.")

if __name__ == "__main__":
    main()



