#!/usr/bin/env python3

import os
import sys
import subprocess

TASKS_FILE = 'tasks.txt'

def update_task(task_id, field, new_value):
    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return
    
    updated = False
    lines = []
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if parts[0] == str(task_id):
                if field == 'title':
                    parts[1] = new_value
                elif field == 'category':
                    parts[2] = new_value
                elif field == 'priority':
                    if new_value.capitalize() not in ['High', 'Medium', 'Low']:
                        print("Invalid priority. Please enter High, Medium, or Low.")
                        sys.exit(1)
                    parts[3] = new_value.capitalize()
                elif field == 'status':
                    if new_value.capitalize() not in ['Pending', 'Completed']:
                        print("Invalid status. Please enter Pending or Completed.")
                        sys.exit(1)
                    parts[4] = new_value.capitalize()
                else:
                    print("Invalid field.")
                    sys.exit(1)
                updated = True
                line = '|'.join(parts) + '\n'
            lines.append(line)
    
    if updated:
        with open(TASKS_FILE, 'w') as file:
            file.writelines(lines)
        print(f"Task ID {task_id} updated successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def main():
    print("=== Update Task ===")
    task_id = input("Enter task ID to update: ").strip()
    print("Fields: title, category, priority, status")
    field = input("Enter field to update: ").strip().lower()
    new_value = input("Enter new value: ").strip()
    
    update_task(task_id, field, new_value)

if __name__ == "__main__":
    main()

