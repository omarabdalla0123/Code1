import tkinter as tk

cor_name = "omer"
cor_password = "1234"

def check():

        name = user_name_entry.get()
        password = user_password_entry.get()

        if name ==cor_name and password == cor_password :
            check_label.config(text = "Thank You For Login")
        else: 
            check_label.config(text = "Wrong User Name Or Password")




root = tk.Tk()
root.title("Simple Login Screen")
root.geometry("500x500")


user_name_label = tk.Label(root, text = "User Name")
user_name_label.place(x = 80, y = 100)

user_password_label = tk.Label(root, text = "User Password")
user_password_label.place(x = 80, y = 130)


user_name_entry = tk.Entry(root)
user_name_entry.place(x = 180, y = 100)

user_password_entry = tk.Entry(root)
user_password_entry.place(x = 180, y = 130)


login_button = tk.Button(root, text = "Login")
login_button.place(x=220, y= 160)



check_label = tk.Label(root, command = check)
check_label.place(x= 250, y = 190)





root.mainloop()