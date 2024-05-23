#!/usr/bin/python3
""" Script that returns employee's TODO list using JSONPlaceholder API """
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userID = sys.argv[1]

    user = '{}users/{}'.format(url, userID)
    res = requests.get(user)
    json_out = res.json()
    name = json_out.get('username')

    todos = '{}todos?userId={}'.format(url, userID)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        l_task.append([userID,
                       name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(userID)
    with open(filename, mode='w') as employeefile:
        employeewriter = csv.writer(employeefile,
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)

        for task in l_task:
            employeewriter.writerow(task)
