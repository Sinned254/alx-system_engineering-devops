#!/usr/bin/python3
"""Use rest api to export data to json format"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetching employee information
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    username = employee_data["username"]

    # Fetching employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Creating JSON data structure
    json_data = {
        str(employee_id): [
            {"task": task["title"], "completed": task["completed"], "username": username}
            for task in todos_data
        ]
    }

    # Exporting data to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file, indent=2)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
