import tkinter as tk
from tkinter import messagebox
root = tk.Tk()


listbox = tk.Listbox(root, height=10, width=10)
listbox.pack()

listbox.insert(tk.END,"Apple")
listbox.insert(tk.END,"Banana")
listbox.insert(tk.END,"Oragne")

listbox.curselection()



def show ():
    selected = listbox.curselection()
    if selected :
        item = listbox.get(selected[0])
        messagebox.showinfo("Selected", f"You chose: {item}")
    else:
        messagebox.showwarning("Warning", "Select an item first!")

button = tk.Button(root, text="show" , command = show)
button.pack()
root.mainloop()