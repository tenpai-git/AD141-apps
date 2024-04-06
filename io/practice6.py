#!/usr/bin/python3
import sys
import os
import time

def readCommandLine():
    a = []
    for i in range(len(sys.argv)):
        if i > 0:
            a.append(sys.argv[i])
    return a

#Read in the flags for the file.
def main():
    cmd_line = readCommandLine()
    target_directory = str(cmd_line[0])
    print("Target Directory is: ", target_directory)
    try:
        target_size_kb = int(cmd_line[1])
    except ValueError:
        print("First value should be a target directory, second value should be an integer in kilobytes to load directory display tool.")
        exit()
    print("Only scanning for items above " + str(target_size_kb) + " kilobytes.")

    # Filter for files with only file size above target_size_kb and print. 
    for a_flag in cmd_line:
        if len(cmd_line) != 2: 
            print("Two parameters are required, the directory and a max filesize to read.")
            exit()

    print("Loading directory display tool...")
    if os.path.exists(target_directory) == True:
        print("Path provided found.")
        print()
        os.chdir(target_directory)
        file_list = os.listdir()
        print("The following files have been found: " + str(file_list))
        print()
        for a_file in file_list:
            if (os.path.getsize(a_file)/1024) >= target_size_kb:
                print()
                print("### File Analysis ###")
                print("Analyzing " + str(a_file))
                print("Total file size in kilobytes is: " + str(int(os.path.getsize(a_file)/1024)))
                file_stat = os.stat(a_file)
                print("Last modified: ", time.ctime(file_stat[8]))
                print()


            else:
                print("### PASS: Skipping " + a_file + " - not above target size.")


    else: 
        print("Path provided not found, exiting program.")
        exit()


#    #Read and open each file.
#    for a_file in files:
#        if a_file == "-t":
#            continue
#        else: 
#            print("Processing: "+ a_file)
#            with open(a_file, "r") as the_file:
#
#

if __name__ == "__main__":
    main()

