#!/usr/bin/python3

import json
import requests

def read_url(url):
    response = requests.get(url)
    print(url)
    print(response.status_code)

    #This needs to be debugged better for url connection error.
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        with open("raw_endpoint_data.json", "w") as raw_data:
            json.dump(data, raw_data, skipkeys=True)
        with open("raw_endpoint_data.json", "r") as raw_data:
            json_data = json.load(raw_data)

        print(json_data["text"])

    else:
        print("Failed on {}, expected 200.".format(response.status_code))
        print("Exiting.")

def main():

    number = input("What integer do you want to lookup?: ")
    url = "http://numbersapi.com/{}/?json&notfound=floor.".format(number)
    math_url = "http://numbersapi.com/{}/math/?json&notfound=floor.".format(number)
    response = requests.get(url)
    read_url(url)
    print()
    read_url(math_url)

if __name__ == "__main__": 
    main()

