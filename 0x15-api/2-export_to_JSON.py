#!/usr/bin/python3
""" Script that returns employee's TODO list using JSONPlaceholder API """
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()

    todo = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todo)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": json_o.get('username')}
        l_task.append(dict_task)

    d_task = {str(sys.argv[1]): l_task}
    filename = '{}.json'.format(sys.argv[1])
    with open(filename, mode='w') as file_:
        json.dump(d_task, file_)
