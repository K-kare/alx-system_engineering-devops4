#!/usr/bin/python3
""" Python to get data from an API and convert to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    res = requests.get(url_user)
    username = res.json().get('username')
    url_task = url_user + '/todos'
    res = requests.get(url_task)
    tasks = res.json()

    dict_data = {user_id: []}
    for task in tasks:
        TASK_FINISHED_STATUS = task.get('completed')
        task_tittle = task.get('title')
        dict_data[user_id].append({
                                  "task": task_tittle,
                                  "finished": TASK_FINISHED_STATUS,
                                  "user": username})
    """print(dict_data)"""
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(dict_data, f)
