import tkinter as tk


def green():
    label.config(fg = "green")


def red():
    label.config(fg = "red")



def blue():
    label.config(fg = "blue")    



root = tk.Tk()

root.title("Color Changer")

root.geometry("500x500")

root.configure(bg="#0D0200")



label = tk.Label(root, text="Hello World !", bg = "white")
label.place(x = 20, y=20)



button = tk.Button(root, text="green", bg="green", fg="white" , command = green)
button.place(x = 20, y=100)



button = tk.Button(root, text="red", bg="red", fg="white", command = red)
button.place(x = 80, y=100)



button = tk.Button(root, text="blue", bg="blue", fg="white", command= blue)
button.place(x = 120, y=100)


root.mainloop()