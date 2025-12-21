#!/usr/bin/env python3
"""
Exports an employee's TODO list to a CSV file
"""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos data
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    # CSV file name
    filename = f"{employee_id}.csv"

    # Write to CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

