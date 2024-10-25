#!/usr/bin/env python3

import os
from prettytable import PrettyTable

TASKS_FILE = 'tasks.txt'

def view_tasks():
    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return
    
    table = PrettyTable()
    table.field_names = ["ID", "Title", "Category", "Priority", "Status"]
    
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 5:
                table.add_row(parts)
    
    print(table)

def main():
    print("=== All Tasks ===")
    view_tasks()

if __name__ == "__main__":
    main()

