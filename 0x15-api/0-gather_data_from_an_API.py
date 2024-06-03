#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    EMPLOYEE_ID = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(EMPLOYEE_ID))
    user_var = user_response.json()
    param = {"userId": EMPLOYEE_ID}
    todo_response = requests.get(url + "todos", params=params)
    todo = todo_response.json()
    completed = []

    for i in todo:
        if i.get("completed") is True:
            completed.append(i.get("tittle"))

    print("Employee {} is done with tasks({}/{})".format(user_var.get("name"), len(completed), len(todo)))

    for complete in completed:
        print("/t {}".format(complete))
