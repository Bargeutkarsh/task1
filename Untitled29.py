

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
        else:
            print("Invalid task index!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index!")

    def display_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {'[done]' if task['completed'] else '[x]'} {task['task']}")


def main():
    todo_list = TodoList()

    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. Remove a task")
        print("4. Display tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()


# In[ ]:




