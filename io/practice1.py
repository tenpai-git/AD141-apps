#!/usr/bin/python3

import sys

#Read in each command line flag as an array element.
def readCommandLine():
    a = []
    for i in range(len(sys.argv)):
        if i > 0:
            #print(str(sys.argv[i]))
            a.append(sys.argv[i])
    return a

#Read in the flags for the file.
def main():
    files = readCommandLine()

    #Read and open each file.
    for a_file in files:
        print("Processing: "+ a_file)
        with open(a_file, "r") as the_file:

            #Perform scans on each file.
            line_count = the_file.readlines() #Read each line of the file into a list.
            word_count = 0 #Create a variable to count each word in the list.
            char_count = 0 #Create a variable for counting each character in the list.             
            for a_line in line_count: #
               word_count += len(a_line.split()) # Counts each word in the line, seperated by space. 
               for a_char in a_line: # Counts each character on the line
                    char_count += 1

            #Prints out the results for the file being processed.
            #Could use refactoring overall.
            print("Line Count: " + str(len(line_count)) + " " + "total line(s) in the file: " + str(a_file))
            print("Word Count: " + str(word_count) + " " + "total word(s) in the file: " + str(a_file))
            print("Character Count: " + str(char_count) + " " + "total character(s) in the file: " + str(a_file))
            print()

if __name__ == "__main__":
    print("#"*30 + "\n" + "Starting File Scan..." + '\n' + "#"*30 + "\n")
    main()
