#!/usr/bin/python3

# Looksup information about book titles in json file format. Format is below:" 

'''
└──╼ $head books.json 
{
  "Things Fall Apart":
    {
      "author": "Chinua Achebe",
      "country": "Nigeria",
      "language": "English",
      "pages": 209,
      "year": 1958
    },
  "Fairy tales":

'''
# Possible Improvements: 
   #Load multiple results into an array for multiple results, and format in a seperate function.
   #Use Regex to search through metadata for matches.
   #Build data sets from web scraping or call the data from an API

import json
import sys

def lookup_book(response, data):

    #Sanitize input for uppercase/lowercase letters.
    for title in data.keys():
        title_check = str(response)
        title_db = str(title)

        #Format output for a matched book. 
        if title_check.lower() == title_db.lower():
            print("Match Found")
            print("#"*97)
            headers = ("Title", "Author", "Country", "Language", "Pages", "Year")
            fmt = "{:20} {:20} {:20} {:10} {:10} {:10}"
            print(fmt.format(*headers))
            print("#"*97)
            print(fmt.format(title, data[title]['author'], data[title]['country'], data[title]['language'], str(data[title]['pages']), str(data[title]['year'])))
            #print("Title: ", title)
            #print("Author: ", data[title]['author'])
            #print("Country: ", data[title]['country'])
            #print("Languages: ", data[title]['language'])
            #print("Pages: ", data[title]['pages'])
            #print("Year: ", data[title]['year'])
            match_flag = True #Kinda useless since we're returning right here, but for more complicated datasets you can put all the results into an array and return the array and format it with a different method, and then send the flag when results are all found. If there were multiple books with the same entries or different editions, for example.  
            return match_flag
        else:
            match_flag = False
    
    if match_flag == False:
        return False

def file_load():

    #Handle file not found error.
    while True: 
        try: 
            #If a file is entered as the first command line argument, it will use that, or ask for input.
            filename = sys.argv[1] if len(sys.argv) > 1 else input("What json file would you like to load for this search?: ")
            with open(filename, 'r') as json_data:
                data = json.load(json_data)
                return data
                break
        except FileNotFoundError:
            print("File not found.", end="\n")
            sys.argv.pop(0) #Prevents infinite loop and triggers above conditional.
            continue

def main():
    data = file_load()
    response = input("Enter a book name to lookup (enter \"quit\" to exit): ")

    while (response != "quit" and response != "exit"):
        if lookup_book(response, data) == True:
            pass
        elif lookup_book(response, data) == False:
            print("Match not found")
        response = input("Enter a book name to lookup (enter \"quit\" to exit): ")

    exit()

if __name__ == "__main__":
    main()
