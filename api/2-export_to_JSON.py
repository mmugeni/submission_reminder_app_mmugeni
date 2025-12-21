#!/usr/bin/env python3
"""
Exports an employee's TODO list to a JSON file
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user info
    user = requests.get(user_url).json()
    username = user.get("username")

    # Fetch todos
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    # Build JSON structure
    data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    # Write JSON file
    with open(f"{employee_id}.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)

