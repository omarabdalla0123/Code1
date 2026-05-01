import tkinter as tk 
import random
import string


def gpassword():
    char = string.ascii_letters + string.digits
    length = int(entry.get())


    password = ""
    for i in  range(length):
        password += random.choice(char)
    
    label.config(text = f"Generated Password : {password}")


root = tk.Tk()

root.title("Simple Password Generator")
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg="#FFFFFF")
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\torn.ico")

entry = tk.Entry(root)
entry.pack()


button = tk.Button(root, text="Generate", command = gpassword)
button.pack()

label = tk.Label(root, text="")
label.pack()



root.mainloop()