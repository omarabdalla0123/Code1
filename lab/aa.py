import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def move_file():
    file = filedialog.askopenfilename()         # pick a file
    destination = "C:/Users/acer/Music/test"
    shutil.move(file, destination)              # move it
    messagebox.showinfo("Done", "File moved!")

root = tk.Tk()
btn = tk.Button(root, text="Move File", command=move_file)
btn.pack()
root.mainloop()
