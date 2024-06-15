#!/usr/bin/python3

import requests
import sys

"""Returns to-do list information for a given employee ID."""

def fetch_employee_data(employee_id):
    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch todos data
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    return user_data, todos_data

def display_todo_progress(employee_id):
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
        return
    
    user_data, todos_data = fetch_employee_data(employee_id)
    
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)
    
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        display_todo_progress(sys.argv[1])
