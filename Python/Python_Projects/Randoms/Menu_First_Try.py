# ---- inputs ----
def To_Do_List():
    tasks = []
    

    while True :
        print("# \n----- To Do List -----#")
        print("1. View Tasks")
        print("2. Add New Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = int(input("Enter The Number from (1-4)"))

        if choice == '1' :
            print("\n YOUR TASKS    ")
            if not tasks :
                print("The List Is Empty")
            else:
                    for  index, task in enumerate(tasks, start=1) :
                        print(f"{index}. {task}")

                    print(tasks)
        elif choice == '2' :
                new_task = input("Enter The New Task Name : ")
                tasks.append(new_task)
        elif choice == '3' :
            if tasks is not None :
                remove_tasks= tasks.remove()
            else :
                print("The List Is Empty")
        elif choice == '4' :
            print('exit')
            break        
To_Do_List