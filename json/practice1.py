#!/usr/bin/python3

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

import json
import time

def lookup_book(response, data):

    for title in data.keys():
        title_check = str(response)
        title_db = str(title)

        if title_check.lower() == title_db.lower():
            print("Match Found")
            print("Title: ", data[title])
            print("Author: ", data[title]['author'])
            print("Country: ", data[title]['country'])
            print("Languages: ", data[title]['language'])
            print("Pages: ", data[title]['pages'])
            print("Year: ", data[title]['year'])

def data_load(filename):
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
        return data

def main():
    filename = input("What json file would you like to load for this search?: ")
    data = data_load(filename)

    response = input("Enter a book name to lookup (enter \"quit\" to exit): ")
    while (response != "quit"):
        lookup_book(response, data)
        response = input("Enter a book name to lookup (enter \"quit\" to exit): ")

    exit()

if __name__ == "__main__":
    main()
