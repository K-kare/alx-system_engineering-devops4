#!/usr/bin/python3
'''
gather employee data from API
'''
import re
import requests
import sys

API_BASE = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(API_BASE, id)).json()
            task = requests.get('{}/todos'.format(API_BASE)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task))
            finished_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(finished_tasks),
                    len(task)
                )
            )
            if len(finished_tasks) > 0:
                for task in finished_tasks:
                    print('\t {}'.format(task.get('title')))
