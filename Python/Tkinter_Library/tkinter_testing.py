import tkinter as tk

def exit():
    root.quit()

root = tk.Tk()

root.geometry("500x500")
root.title("Menus Test")
root.configure(bg="#FFFFFF")
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\Photos\torn.ico")
root.resizable(False,False)

menubar = tk.Menu(root, tearoff = 0)
root.config(menu=menubar)


file_menu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu=file_menu)
file_menu.add_separator()

file_menu.add_command(label = "Exit", command = exit)


root.mainloop()