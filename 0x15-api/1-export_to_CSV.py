#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys


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


def export_to_csv(employee_id):
    user_data, todos_data = fetch_employee_data(employee_id)
    
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in todos_data:
            writer.writerow([
                user_data.get('id'),
                user_data.get('username'),
                task.get('completed'),
                task.get('title')
            ])
    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        display_todo_progress(employee_id)
        export_to_csv(employee_id)
