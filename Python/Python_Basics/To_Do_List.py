
tasks = []


def add(task) :
    task =input("Enter The Task Name : ")
    tasks.append(task)



def show():
    print(f"Tasks : {tasks}")


def quit1() :
    exit()



def remove():
    if tasks == [] :
        print("The list is empty")
        exit()
    else :
        task = input("Enter task name : ")
        if task in tasks :
            tasks.remove(task)



while True :
    task = input(" Choose from this Options\n (a) to add \n (r) to remove " + 
            "\n (s) to show the list \n (q) to quit \n Your choice : ") 
    if task == "a" :
        res = add(task)
    elif task == "s":
        res = show()
    elif task == "q":
        res = quit1()
    elif task == "r":
        res = remove()
    else :
        print("only one of [a, s, r, q]")



# task == "a":
#     res = add(task)
# elif task == "s" :
#     res = show()    

# print(tasks)


