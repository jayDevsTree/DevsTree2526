import json
import os
import logging

logging.basicConfig(filename='tasks_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tasks = []
file_path = "tasks.json"

class EmptyValueException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'{self.message}'

class EmptyValueHelper:
    @staticmethod
    def empty_title():
        return EmptyValueException("Task title cannot be empty! Re-enter title:")

    @staticmethod
    def empty_description():
        return EmptyValueException("Task description cannot be empty! Re-enter description:")

    @staticmethod
    def empty_status():
        return EmptyValueException("Task status cannot be empty! Re-enter status:")

class Task:

    def read_tasks_from_file():
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        tasks[:] = [t for t in data if isinstance(t, dict)]# this check every t must be dictonary 
                    else:
                        tasks[:] = []
            except json.JSONDecodeError:
                tasks[:] = []
        else:
            tasks[:] = []
        return tasks

    def valid_task(existing_id=None):
        temp = {}
        temp['id'] = existing_id if existing_id else len(tasks) + 1

        # if existing_id:
        #     temp['id'] = existing_id
        # else:
        #     temp['id'] = len(tasks) + 1
            
        while True:
            try:
                title = input("Enter Task Title: ")
                if title == "":
                    raise EmptyValueHelper.empty_title()
                temp['title'] = title
                break
            except EmptyValueException as e:
                print(e)

        while True:
            try:
                desc = input("Enter Task Description: ")
                if desc == "":
                    raise EmptyValueHelper.empty_description()
                temp['description'] = desc
                break
            except EmptyValueException as e:
                print(e)

        while True:
            try:
                print("Status options:[Ongoing, Completed, Pending] or Custom Status")
                status = input("Enter Task Status: ")
                if status == "":
                    raise EmptyValueHelper.empty_status()
                temp['status'] = status
                break
            except EmptyValueException as e:
                print(e)

        return temp

    def valid_id():
        Task.read_tasks_from_file()
        while True:
            user_id = input("Enter the task id: ")
            try:
                valid_user_id = int(user_id)
                if valid_user_id <= 0 or valid_user_id > len(tasks):
                    print("Invalid input! Please enter a valid task id.")
                    continue
                return valid_user_id
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def add_task():
        Task.read_tasks_from_file()
        new_task = Task.valid_task()
        tasks.append(new_task)
        Task.write_task()
        print("Task Added Successfully!")

    def view_task():
        Task.read_tasks_from_file()
        print(tasks)

    def update_task(update_id):
        Task.read_tasks_from_file()
        for i, task in enumerate(tasks):
            if task['id'] == update_id:
                tasks[i] = Task.valid_task(existing_id=update_id)
                Task.write_task()
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(delete_id):
        Task.read_tasks_from_file()
        for task in tasks:
            if task['id'] == delete_id:
                tasks.remove(task)
                Task.write_task()
                print("Task deleted successfully.")
                return
        print("Task not found.")

    def write_task():
        with open(file_path, 'w') as file:
            json.dump(tasks, file, indent=4)

def wrapped_task_class():
    while True:
        print()
        print('''1 --> Add Task
2 --> View Task
3 --> Update Task
4 --> Delete Task
(press anything else to Exit)''')

        user_choice = input("Enter Choice: ")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Thank You!")
            break

        if user_choice == 1:
            Task.add_task()
        elif user_choice == 2:
            Task.view_task()
        elif user_choice == 3:
            update_id = Task.valid_id()
            Task.update_task(update_id)
        elif user_choice == 4:
            delete_id = Task.valid_id()
            Task.delete_task(delete_id)
        else:
            print("Thank You!")
            break

if __name__ == "__main__":
    Task.read_tasks_from_file()
    wrapped_task_class()
