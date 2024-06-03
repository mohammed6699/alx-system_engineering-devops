#!/usr/bin/python3

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_response = requests.get(url + "user/{}".format(user_id))
    eser = user_response.json()
    USERNAME = user.get("USERNAME")
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    with open ("{}.csv".format(user_id), "w", newline="")as csvfile:
        writer = csv.writer(csvfile, quoting=CSV.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id, USERNAME, todo.get("completed"), todo.get("title")])