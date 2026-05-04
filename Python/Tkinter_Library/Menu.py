import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("New","Awear")

def about():
    messagebox.showinfo("New","Awear")    
root = tk.Tk()
root.geometry("500x500")
root.title("Menus")
root.resizable(False,False)
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\Photos\torn.ico")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)



file_menu.add_command(label="New", command=new_file)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

root.mainloop()