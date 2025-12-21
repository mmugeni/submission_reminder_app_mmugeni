#!/usr/bin/env python3
"""
Fetches and displays an employee's TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    # Get employee ID from command line
    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos data
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    # Calculate totals
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    number_done = len(completed_tasks)

    # Print header
    print(
        f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):"
    )

    # Print completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

