#!/usr/bin/env python3

import os
import sys

TASKS_FILE = 'tasks.txt'

def get_next_id():
    if not os.path.exists(TASKS_FILE):
        return 1
    with open(TASKS_FILE, 'r') as file:
        lines = file.readlines()
        if not lines:
            return 1
        last_id = int(lines[-1].split('|')[0])
        return last_id + 1

def add_task(title, category, priority):
    task_id = get_next_id()
    with open(TASKS_FILE, 'a') as file:
        file.write(f"{task_id}|{title}|{category}|{priority}|Pending\n")
    print(f"Task '{title}' added with ID {task_id}.")

def main():
    print("=== Add New Task ===")
    title = input("Enter task title: ").strip()
    category = input("Enter category (Work/Personal/etc.): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    
    if priority not in ['High', 'Medium', 'Low']:
        print("Invalid priority. Please enter High, Medium, or Low.")
        sys.exit(1)
    
    add_task(title, category, priority)

if __name__ == "__main__":
    main()

