#!/usr/bin/env python3

import os
import sys

TASKS_FILE = 'tasks.txt'

def delete_task(task_id):
    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return
    
    deleted = False
    lines = []
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if parts[0] != str(task_id):
                lines.append(line)
            else:
                deleted = True
    
    if deleted:
        with open(TASKS_FILE, 'w') as file:
            file.writelines(lines)
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def main():
    print("=== Delete Task ===")
    task_id = input("Enter task ID to delete: ").strip()
    confirm = input(f"Are you sure you want to delete task ID {task_id}? (y/n): ").strip().lower()
    if confirm == 'y':
        delete_task(task_id)
    else:
        print("Deletion canceled.")

if __name__ == "__main__":
    main()

