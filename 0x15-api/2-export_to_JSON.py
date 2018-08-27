#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import json
from collections import OrderedDict
import requests
import sys


def get_user_todo():
    '''
    get user todo
    '''
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(sys.argv[1]))
    name = emp.json().get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))
    tasks = tasks.json()
    res = []
    final_id = OrderedDict()
    filename = sys.argv[1] + ".json"

    with open(filename, 'w+') as f:
        for task in tasks:
            final = OrderedDict()
            final['task'] = task['title']
            final['completed'] = task['completed']
            final['username'] = name
            res.append(final)
        final_id[sys.argv[1]] = res
        json.dump(final_id, f)


if __name__ == "__main__":
    get_user_todo()
