import tkinter as tk

tasks = []
y_position = 10  # starting y position

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

def remove():
    global y_position
    for var, cb in tasks:
        if var.get() == 1:
            cb.destroy()
    tasks[:] = [(var, cb) for var, cb in tasks if var.get() != 1]
    y_position = 10
    for var, cb in tasks:
        cb.place(x=10, y=y_position)
        y_position += 30  # repositions remaining tasks

root = tk.Tk()
root.title("To Do List")
root.geometry("500x600")
root.configure(bg="#2C2F33")

tk.Label(root, text="To Do List", bg="#2C2F33", fg="white",
         font=("Arial", 20, "bold")).place(x=180, y=10)

entry = tk.Entry(root, bg="#23272A", fg="white", font=("Arial", 12),
                 insertbackground="white", width=30)
entry.place(x=100, y=60)

tk.Button(root, text="Add Task", bg="#7289DA", fg="white",
          font=("Arial", 12), border=0, width=15, command=add).place(x=100, y=100)

tk.Button(root, text="Remove Checked", bg="#F04747", fg="white",
          font=("Arial", 12), border=0, width=15, command=remove).place(x=260, y=100)

frame = tk.Frame(root, bg="#23272A", width=400, height=350)
frame.place(x=50, y=140)

root.mainloop()