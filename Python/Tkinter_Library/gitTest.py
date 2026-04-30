import tkinter as tk


def on_button_click():
    label.config(text="Button Clicked!")



root = tk.Tk()
root.title("Git Test")
root.geometry("500x500")
root.configure(bg="lightblue")
root.resizable(False, False)
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\torn.ico")


label = tk.Label(root, text="Hello, Git!", font=("Arial", 24), bg="lightblue", fg="darkblue")
label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

button = tk.Button(root, text="Click Me", font=("Arial", 16), bg="white", fg="black" , command =on_button_click)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
