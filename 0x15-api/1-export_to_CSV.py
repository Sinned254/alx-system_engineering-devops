#!/usr/bin/python3
import requests
import csv
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetching employee information
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetching employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Exporting data to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

        # Writing tasks data
        for task in todos_data:
            writer.writerow([
                f"{user_id}",
                f'{username}',
                f'{str(task["completed"])}',
                f'{task["title"]}'
            ])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
