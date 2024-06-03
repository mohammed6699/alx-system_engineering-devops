#!/usr/bin/python3

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_response = requests.get(url + "user/{}".format(user_id))
    user = user_response.json()
    data_to_export = {user_id :[]}

    for todo in todos:
        task_info = {
                "task": todo.get("title")
                comleted: todo.get("completed")
                "USERNAME": USERNAME
                }
        data_to_export[user_id].append(task_info)

    with open ("{}.json".format(user_id), "w", newline="")as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
