#!/usr/bin/python3
""" Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user
    req = requests.get(user_url)
    """ANYTHING"""
    user_name = req.json().get('username')
    task = user_url + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            done = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, done, title_task))
