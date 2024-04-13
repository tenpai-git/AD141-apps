#!/usr/bin/python3
import sys
import string

def readCommandLine():
    a = []
    for i in range(len(sys.argv)):
        if i > 0:
            a.append(sys.argv[i])
    return a

def main():

    files = readCommandLine()
    if len(files) <= 1:
        print("Please provide more than one file name for comparison.")
        exit()
    else:

        #Create comparison file of all names in all files
        try:
            #Loop over each file
            for input_file in files:
                with open(input_file, "r") as input:
                    current_stream = input.readlines()
                    #Add the line for each file to comparison file
                    for line in current_stream:
                        with open("comparisonfile", "a") as comparison_file:
                            comparison_file.write(str(line))
                    #Add a new line in between each file written array
                    with open("comparisonfile", "a") as comparison_file:
                        comparison_file.write("\n")

            #Read new file
            with open("comparisonfile", "r+") as source_file:
                count_stream = source_file.readlines()
                #This will remove duplicates and sort from this stream since we only need to check unique values.
                count_stream.sort()
                count_stream = set(count_stream)
                #For each line in the source file
                for line in count_stream:
                    name_count = int()

                    #Open a copy of the source file 
                    with open("comparisonfile", "r+") as comparison_file:
                        compare_stream = comparison_file.readlines()





                    #Count the amount of times the line shows up in the file. It will count itself.
                    for comparison_line in compare_stream:
                        if line == comparison_line:
                            name_count += 1 #Occurences of the name. 

                    for comparison_line in compare_stream:
                        if line == comparison_line:
                            new_line = line.strip()
                            print(f"{new_line}: {name_count}")
                            break



                    


                        
#
#                            with open("name_counter_output", "w") as output_file:
#                                new_line = line.strip()
#                                print(f"{new_line}: {name_count}")
#                                output_file.write(str(line) + ": " + str(name_count))
#                        
#                        #Remove the name from the comparison file so it's not iterated over again.
#                            
#                        #If the comparison line is not the same, write it to the new file stream.
#                        if comparison_line != line:
#                            new_compare_stream.append(comp_line)
#
#                        #Overwrite the file stream. 
#                    compare_stream = new_compare_stream
#                            #compare_stream.remove(comparison_line)
#                            #source_file.write(str(compare_stream))
#
#                    with open("name_counter_output", "w") as output_file:
#                        output_file.write(str(line) + ": " + str(name_count))
#
#
#                    for comp_line in compare_stream:
#                        if comp_line != line:
#                            new_compare_stream.append(comp_line)
#                    compare_stream = new_compare_stream

        except FileNotFoundError as err:
            print("Invalid input file. This file must exist in this directory already.")

if __name__ == "__main__":
    main()



