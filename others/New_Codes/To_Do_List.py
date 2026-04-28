# List  
#Functions
 #Loops
# Menu Systems
tasks =[]

def show_menu():
    print("\n---To Do List ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully")
def view_tasks():
    if not tasks:
        print("NO tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks1, start=1):
            print(f"{i}. {task}")
def delete_task():
    view_tasks()
    if tasks:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Removed task: {removed}")
        else :
            print("Invalid task number.")
while True:
    show_menu()
    choice = input("choose an option: ")
    
    if choice == "1":
         add_task()
    elif choice == "2":
         view_tasks()
    elif choice == "3":
         delete_task()
    elif choice == "4":
         print("Goodby 👋")
         break
    else:
        print("Invalid choice, try again.")