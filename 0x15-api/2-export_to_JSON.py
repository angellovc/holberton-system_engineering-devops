#!/usr/bin/python3
"""  export data from JSONPlaceholder into JSON format """
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r.json()
    for user in users:
        if user.get('id') == int(argv[1]):
            user_name = user.get('username')
            user_id = user.get('id')
            break

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = r.json()
    user_content = {}
    user_content[str(user_id)] = []
    for todo in todos:
        task = {}
        if todo.get('userId') == user_id:
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            task['username'] = user_name
            user_content[str(user_id)].append(task)

    json_file = str(user_id)+".json"

    with open(json_file, mode='w', encoding="UTF8") as j_file:
        json.dump(user_content, j_file)
