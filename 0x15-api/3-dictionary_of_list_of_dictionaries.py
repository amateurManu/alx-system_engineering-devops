#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information on employees """
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    d_task = {}
    for user in res.json():
        name = user.get('username')
        userID = user.get('id')
        todo = '{}todos?userId={}'.format(url, userID)
        res = requests.get(todo)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(userID)] = l_task

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file_:
        json.dump(d_task, file_)
