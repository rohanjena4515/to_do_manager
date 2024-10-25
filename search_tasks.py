#!/usr/bin/env python3

import os
import sys
from prettytable import PrettyTable
import subprocess

TASKS_FILE = 'tasks.txt'

def search_tasks(keyword, field):
    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return
    
    table = PrettyTable()
    table.field_names = ["ID", "Title", "Category", "Priority", "Status"]
    matched = False
    
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 5:
                if field == 'all':
                    if keyword.lower() in line.lower():
                        table.add_row(parts)
                        matched = True
                elif field == 'id' and parts[0] == keyword:
                    table.add_row(parts)
                    matched = True
                elif field == 'title' and keyword.lower() in parts[1].lower():
                    table.add_row(parts)
                    matched = True
                elif field == 'category' and keyword.lower() in parts[2].lower():
                    table.add_row(parts)
                    matched = True
                elif field == 'priority' and keyword.lower() == parts[3].lower():
                    table.add_row(parts)
                    matched = True
                elif field == 'status' and keyword.lower() == parts[4].lower():
                    table.add_row(parts)
                    matched = True
    
    if matched:
        print(table)
    else:
        print("No matching tasks found.")

def main():
    print("=== Search Tasks ===")
    print("Search by fields: all, id, title, category, priority, status")
    field = input("Enter field to search by: ").strip().lower()
    keyword = input("Enter keyword to search: ").strip()
    
    valid_fields = ['all', 'id', 'title', 'category', 'priority', 'status']
    if field not in valid_fields:
        print("Invalid field.")
        sys.exit(1)
    
    search_tasks(keyword, field)

if __name__ == "__main__":
    main()

