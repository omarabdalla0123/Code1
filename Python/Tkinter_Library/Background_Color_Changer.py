import tkinter as tk




def change_color():

    color = (entry.get()).lower()

    if color == "red":
        root.configure(bg="red")
        label.pack_forget()
    elif color == "green" :
        label.pack_forget()
        root.configure(bg="green")
    elif color == "blue" :
        label.pack_forget()
        root.configure(bg="blue")
    else:
        root.configure(bg = "#FFFFFF")
        label.config(text= "Choose form (red, green and blue) only")



root =  tk.Tk()

root.geometry("500x500")
root.title("Color Changer")
root.resizable(False,False)

root.configure(bg = "#FFFFFF")


entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text= "")
label.pack()

button = tk.Button(root, text = "Change", command = change_color)
button.pack()

root.mainloop()