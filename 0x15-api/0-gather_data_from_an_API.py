#!/usr/bin/python3
""" Script that returns employee's TODO list using JSONPlaceholder API """
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_out = res.json()
    print("Employee {} is done with taks".format(json_out.get('name')), end="")

    todo = '{}todos?userID={}'.format(url, sys.argv[1])
    res = requests.get(todo)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
