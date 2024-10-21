# To-Do list 

import json
import os

# Class for individual tasks
class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    # Convert the task to a dictionary for JSON storage
    def to_dict(self):
        return {"description": self.description, "done": self.done}

    # Create a Task from a dictionary (loaded from JSON)
    @staticmethod
    def from_dict(data):
        return Task(data["description"], data["done"])

# Class to manage the task list
class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # Load tasks from a file if it exists, otherwise return an empty list
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                tasks_data = json.load(f)
                return [Task.from_dict(task) for task in tasks_data]
        return []

    # Save all tasks to the file in JSON format
    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    # Add a new task
    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{description}' has been added.\n")

    # Remove a task by index
    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task '{removed_task.description}' has been removed.\n")
        except IndexError:
            print("Invalid task number.\n")

    # Mark a task as done
    def mark_task_done(self, index):
        try:
            self.tasks[index].mark_done()
            self.save_tasks()
            print(f"Task '{self.tasks[index].description}' is now marked as complete.\n")
        except IndexError:
            print("Invalid task number.\n")

    # Display all tasks
    def show_tasks(self):
        if not self.tasks:
            print("No tasks remaining.\n")
        else:
            print("\nRemaining tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = "✓" if task.done else "✗"
                print(f"{i}. {task.description} [{status}]")
            print()

# Function for the menu, run with simple commands
def menu():
    manager = TaskManager()

    while True:
        print("----- Task Manager -----")
        print("1. Show pending tasks")
        print("2. Add a new task")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            description = input("Enter new task: ")
            manager.add_task(description)
        elif choice == "3":
            manager.show_tasks()
            try:
                task_number = int(input("Which task do you want to mark as complete (enter number)? ")) - 1
                manager.mark_task_done(task_number)
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "4":
            manager.show_tasks()
            try:
                task_number = int(input("Which task do you want to remove (enter number)? ")) - 1
                manager.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.\n")

# Simple code to run the program
if __name__ == "__main__":
    menu()