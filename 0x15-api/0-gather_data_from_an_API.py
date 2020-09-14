#!/usr/bin/python3
""" returns information about his/her TODO list progress """
import requests
from sys import argv


r = requests.get('https://jsonplaceholder.typicode.com/users')
users = r.json()
for user in users:
    if user['id'] == int(argv[1]):
        user_name = user['name']
        user_id = user['id']
        break

r = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = r.json()

total_tasks = 0
completed = 0
tasks = []

for todo in todos:
    if todo['userId'] == user_id:
        total_tasks += 1
        if todo['completed'] is True:
            completed += 1
            tasks.append(todo['title'])

print("Employee {} is done with tasks({}/{}):".format(
    user_name,
    completed,
    total_tasks)
)
for task in tasks:
    print("     "+task)
