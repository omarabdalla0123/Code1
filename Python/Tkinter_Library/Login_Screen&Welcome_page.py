import tkinter as tk

name_co = "omer"

password_co = "1234"

def check():
    
    user_name = userNameEntry.get()
    user_password = userPasswordEntry.get()

    if user_name == name_co and user_password == password_co :
        userNameEntry.place_forget()
        userNameLabel.place_forget()
        userPasswordEntry.place_forget()
        userPasswordLabel.place_forget()

        label.config(text="Welcome Omer !")
    else:
        label.config(text="No")    

root = tk.Tk()
root.title("Login Screen & Welcome Page")

root.geometry("500x500")


userNameLabel = tk.Label(root, text= " User Name ")
userNameLabel.place(x=10,y=50)

userNameEntry = tk.Entry(root)
userNameEntry.place(x=120,y=50)


userPasswordLabel = tk.Label(root, text= " User Password ")
userPasswordLabel.place(x=10,y=100)

userPasswordEntry = tk.Entry(root)
userPasswordEntry.place(x=120,y=100)


tk.Button(root, text = "Login ", command = check).place(x=130,y=150)


label = tk.Label(root, text="")
label.place(x=130,y=190)

root.mainloop()