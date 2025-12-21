#!/usr/bin/env python3
"""
Exports all employees' TODO lists to a JSON file
"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users and todos
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Map user ID to username
    user_map = {user["id"]: user["username"] for user in users}

    # Build final structure
    all_tasks = {}

    for task in todos:
        user_id = str(task.get("userId"))

        if user_id not in all_tasks:
            all_tasks[user_id] = []

        all_tasks[user_id].append({
            "username": user_map.get(task.get("userId")),
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    # Write JSON file
    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(all_tasks, json_file)

