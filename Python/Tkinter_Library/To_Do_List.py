import tkinter as tk 
import os

tasks = []
y_position = 10

def load_tasks():
    if os.path.exists("Tasks.txt") :
        with open("Tasks.txt", "r") as file:
            for line in file :
                listbox.insert(tk.END, line.strip())


def save_tasks():
    with open("tasks.txt" ,"w") as file :
        for i in range(listbox.size()) :
            file.write(listbox.get(i) + "\n")


def add():
    global y_position
    task = entry.get()
    if task != "":
        var = tk.IntVar()
        cb = tk.Checkbutton(frame, text=task, variable=var,
                            bg="#23272A", fg="white",
                            selectcolor="#23272A",
                            activebackground="#23272A")
        cb.place(x=10, y=y_position)
        tasks.append((var, cb))
        entry.delete(0, tk.END)
        y_position += 30  # moves down for the next task
    else:
        label.config(text = "! You Didn't Enter Anything !", bg = "#2C2F33", fg = "white" )
def remove():
    for var, cb in tasks :
        if var.get() == 1: 
            cb.destroy()
    tasks[:] = [(var,cb)   for var, cb in tasks if var.get() != 1]


def clear():
    os.remove("tasks.txt")


root = tk.Tk()
root.title("Simple To Do List")
root.geometry("1000x1000")
root.configure(bg="#2C2F33")


task_label = tk.Label(root, text= "Enter Your New Task Name : ", bg = "#2C2F33", font =("Arial"), fg = "white")
task_label.place(x = 22, y = 90)

entry = tk.Entry(root, bg="#23272A", fg="white", font=("Arial"), insertbackground="white")
entry.place(x = 294, y = 90)
tk.Button(root, text = "Add", bg = "#7289DA", fg = "white", font= ("Arial"),border = 0,command = add).place(x =294 , y = 390 )
tk.Button(root, text = "remove", bg = "#7289DA", fg = "white", font= ("Arial"),border = 0,  command = remove).place(x = 390, y =390 )

tk.Button(root, text = "Clear", bg = "#7289DA", fg = "white", font= ("Arial"),border = 0,  command = clear).place(x = 490, y =390 )



listbox = tk.Listbox(root, bg="#23272A", fg="white", font=("Arial"), border=0, selectbackground="#7289DA")
listbox.place(x =294 , y = 120)


checkbox = tk.Checkbutton(root, text = "yes")
checkbox.place(x=22 , y = 300)

load_tasks()
label = tk.Label(root, text = " ", bg = "#2C2F33")
label.place(x = 22, y = 160)

frame = tk.Frame(root)
frame.place(x=50, y=140)

root.mainloop()