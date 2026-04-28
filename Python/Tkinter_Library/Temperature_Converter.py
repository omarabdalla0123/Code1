import tkinter as tk





def c():
    user = int(entry.get())

    user = (user - 32) * 5/9

    label.config(text= f"Result : {user}")

def f():
    user = int(entry.get())

    user = (user * 9/5) + 32

    label.config(text= f"Result : {user}")




root = tk.Tk()

root.title("Temperature Converter")

root.geometry("500x500")

root.configure(bg="#0D0200")

entry = tk.Entry(root)
entry.place(x = 50, y = 50)



tk.Button(root, text = "Celsuis", bg="#84FB05", fg="#FFFFFF", command = c).place(x = 50, y = 100)

tk.Button(root, text = "Fahrenheit", bg="#3605FA", fg="#FFFFFF", command = f).place(x = 140, y = 100)



label = tk.Label(root, text="Result :",bg="gray",fg="white")
label.place(x=230,y=150)

root.mainloop()