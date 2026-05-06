import tkinter as tk

count =0

def add():
    global count
    count = count+1 
    label.config(text=f"Num : {count}")

def remove():
    global count
    count = count - 1 
    label.config(text=f"Num : {count}")



def rest():
    global count
    count = 0
    label.config(text =f"Num : {count}")



root = tk.Tk()

root.title("Simple Counter")

root.geometry("500x500")

root.configure(bg= "#0D0200")


label = tk.Label(root, text=f"Num : {count}")
label.place(x=45,y=40)
tk.Button(root, bg="green", fg="blue", text= "+", command = add).place(x=20,y=100)

tk.Button(root, bg="green", fg="blue", text= "-", command=remove).place(x=80,y=100)


tk.Button(root, bg="green", fg="blue", text= "Rest", command=rest).place(x=140,y=100)



root.mainloop()

