#!/usr/bin/python3
"""  export data from JSONPlaceholder into JSON format """
import csv
import json
import requests


def todo_from_user(todo, user_name, user_id):
    tasks = []
    for todo in todos:
        task = {}
        if todo.get('userId') == user_id:
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            task['username'] = user_name
            tasks.append(task)
    return tasks


if __name__ == "__main__":

    json_file = "todo_all_employees.json"

    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r.json()
    user_content = {}
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = r.json()

    for user in users:
        user_id = user.get('id')
        user_content[str(user_id)] = todo_from_user(
            todos,
            user.get('username'),
            user_id
        )

    with open(json_file, mode='w', encoding="UTF8") as j_file:
        json.dump(user_content, j_file)
