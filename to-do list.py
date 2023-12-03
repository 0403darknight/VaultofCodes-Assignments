import os
def add_task(tasks, description, due_date):
    tasks.append({"description":description, "due_date":due_date})
def view_tasks(tasks):
    if not tasks:
        print("No Tasks Found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}.{task['description']}- Due Date: {task['due_date']}")
def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index-1]
        print("Tasks Deleted Successfully")
    else:
        print("Invalid Task")
def save_task_to_file(tasks, file_path):
    with open(file_path, 'w') as f:
        for task in tasks:
            f.write(f"{task ['description']}|{task['due_date']}\n ")
def load_task_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                description, due_date = line.strip().split('|')
                tasks.append({"description": description, "due_date": due_date})
    return tasks
def main():
    tasks = []
    file_path = "task.txt"
    tasks = load_task_from_file(file_path)
    while True:
        print("\nOptions:")
        print("1. ADD TASK")
        print("2. VIEW TASK")
        print("3. DELETE TASK")
        print("4. EXIT")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter Due Date: ")
            add_task(tasks, description, due_date)
            save_task_to_file(tasks, file_path)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            task_index = int((input("Enter the task index to delete: ")))
            delete_task(tasks, task_index)
            save_task_to_file(tasks, file_path)
        elif choice =='4':
            print("Exiting the To-Do list!!")
            break
        else:
            print("Invalid Choice. Try Again")

if __name__ == "__main__":
    main()
