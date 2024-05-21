#!/usr/bin/python3
"""python script to fetch Rest API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    Users = resp.json()

    users_dict = {}
    for user in Users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        resp = requests.get(url)

        tasks = resp.json()
        users_dict[user_id] = []
        for task in tasks:
            task_finished = task.get('completed')
            task_tittle = task.get('title')
            users_dict[user_id].append({
                "task": task_tittle,
                "finished": task_finished,
                "username": username
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
