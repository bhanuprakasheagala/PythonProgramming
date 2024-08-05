import os

tasks = []

def display_menu():
  print("\nPersonal Task Manager")
  print("1. Add Task")
  print("2. View Task")
  print("3. Delete Task")
  print("4. Mark Task as completed")
  print("5. Save tasks")
  print("6. load_tasks")
  print("7. Exit")

def add_task(task):
  tasks.append({"task": task, "Completed": False})
  print(f"Task '{task}' added.")

def view_tasks():
  print("\nTasks List")
  for index, task in enumerate(tasks):
    status = "Completed" if task["completed"] else "Not completed"
    print(f"{index + 1}. {task['task']} - {status}")

def delete_task(task_number):
  if 0 < task_number <= len(tasks):
    removed_task = tasks.pop(task_number - 1)
    print(f"Task '{removed_task['task']}' deleted. ")
  else:
    print("Invalid task number")

def mark_task_completed(task_number):
  if 0 < task_number <= len(tasks):
    tasks[task_number - 1]["completed"] = True
    print(f"Task  '{tasks[task_number - 1]['task']}' marked as completed.")
  else:
    print("Invalid task number")

def save_tasks():
  with open('tasks.txt', 'w') as file:
    for task in tasks:
      file.write(f"{task['task']}|{task['completed']}\n")
def load_tasks():
  if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as file:
      for line in file:
        task, completed = line.strip().split('|')
        tasks.append({"task": task, "completed": completed == 'True'})

def main():
  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      task = input("Enter task: ")
      add_task(task)
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      view_tasks()
      task_number = int(input("Enter task number to delete: "))
      delete_task(task_number)
    elif choice == '4':
      view_tasks()
      task_number = int(input("Enter task number to mark as completed: "))
      mark_task_complete(task_number)
    elif choice == '5':
      save_tasks()
    elif choice == '6':
      load_tasks()
    elif choice == '7':
      print("Exiting....")
      break
    else:
      print("Invalid choice!!")

if __name__ == "__main__":
  main()
