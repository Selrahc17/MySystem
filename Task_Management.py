import time  # Importing a module

# Global variable
global_task_counter = 0

# Class definition
class TaskManager:
    def __init__(self):
        # Define default tasks
        self.tasks = ["Buy groceries", "Finish homework", "Clean the house"]

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            print(f"Task added: {task}")
        else:
            raise ValueError("Task cannot be empty!")

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            print(f"Task removed: {task}")
        except ValueError:
            print(f"Task not found: {task}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available!")
        else:
            print("Current tasks:")
            for task in self.tasks:
                print(f"- {task}")

# Function for task management with user input
def manage_tasks():
    manager = TaskManager()

    # Display default tasks
    print("Default tasks:")
    manager.show_tasks()

    # Ask the user how many tasks they want to add
    num_tasks = int(input("How many additional tasks would you like to add? "))
    for _ in range(num_tasks):
        task = input("Enter a task: ")
        manager.add_task(task)

    # Display tasks after addition
    print("\nUpdated task list:")
    manager.show_tasks()

    # Ask if they want to remove a task
    remove_task = input("Do you want to remove any task? (yes/no): ").strip().lower()
    if remove_task == 'yes':
        task_to_remove = input("Enter the task to remove: ")
        manager.remove_task(task_to_remove)
        print("\nUpdated task list after removal:")
        manager.show_tasks()

    return manager  # Return the manager to use its task list

# Main logic
def main():
    global global_task_counter  # Declare the global variable

    # Perform task operations
    manager = manage_tasks()

    # Update global task counter after managing tasks
    global_task_counter += len(manager.tasks)  # Count tasks managed

    # Write to a file
    with open("tasks_log.txt", "w") as file:
        file.write(f"Managed {len(manager.tasks)} tasks.\n")
        file.write("Tasks managed: \n")
        for task in manager.tasks:
            file.write(f"- {task}\n")

    print(f"Global task counter updated: {global_task_counter}")

    # Example of using 'assert' to check task count
    assert global_task_counter > 0, "No tasks managed!"

    # Print final message
    print("Task management completed.")

if __name__ == "__main__":
    main()
