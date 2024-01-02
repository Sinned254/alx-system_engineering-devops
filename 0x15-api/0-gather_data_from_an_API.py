#!/usr/bin/python3
""" Fetches Employee data from an API and displays on the page.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Gets username
       Args:
           employee_id (str): user id number
       Returns: employee id
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetching employee information
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetching employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Counting completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(task["completed"] for task in todos_data)

    # Displaying employee TODO list progress
    print(f"Employee {employee_name} is done with tasks
          ({completed_tasks}/{total_tasks}): ")

    # Displaying completed tasks
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
