#!/usr/bin/python3

import json
import requests

def main():

    #The JSON Data should be formatted as minimally as possible (no spaces, no newlines, etc):
    seps = (',', ':')

    #Get the task list as JSON from the API URL.
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    total_tasks = 0
    completed_tasks = 0
    if response.status_code == 200:
        #Save the data to two local files, one that contains completed tasks and another one that contains incomplete tasks.
        data = json.loads(response.content.decode())
        with open("raw_api_data.json", "w") as raw_data:
            json.dump(data, raw_data, skipkeys=True, separators=seps)
        with open("raw_api_data.json", "r") as raw_data:
            data = json.load(raw_data)
        for task in data: 
            total_tasks += 1
            if task["completed"] == True: 
                completed_tasks += 1
                with open("api_data_completed.json", "w") as raw_completed_data:
                    json.dump(data, raw_completed_data, skipkeys=True, separators=seps)
            else: 
                with open("api_data_incomplete.json", "w") as raw_incompleted_data:
                    json.dump(data, raw_incompleted_data, skipkeys=True, separators=seps)
        print("Files parsed and loaded.")
    else:
        print("response status:", response.status_code)
        print("Done")

    #The program should display the number of tasks we have completed.
    print("There are {} out {} tasks completed.".format(str(completed_tasks), str(total_tasks)))

if __name__ == "__main__": 
    main()

