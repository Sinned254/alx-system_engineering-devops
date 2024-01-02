#!/usr/bin/python3
"""script to gather all todo data from an API and write to JSON file"""
import requests
import json


def export_todo_all_employees():
    base_url = "https://jsonplaceholder.typicode.com/users"

    # Fetching information for all employees
    employees_response = requests.get(base_url)
    employees_data = employees_response.json()

    # Creating a dictionary to store data for all employees
    all_employees_data = {}

    for employee in employees_data:
        employee_id = employee["id"]
        username = employee["username"]
        todos_url = f"https://jsonplaceholder.typicode.com/" \
                    f"todos?userId={employee_id}"

        # Fetching employee's TODO list
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Adding tasks data to the dictionary
        all_employees_data[str(employee_id)] = [
            {"username": username,
             "task": task["title"],
             "completed": task["completed"]}
            for task in todos_data
        ]

    # Exporting data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)


if __name__ == "__main__":
    export_todo_all_employees()
