import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):

    def __init__(self,parent):
        super().__init__(parent)


        self.co_user_name = "omer"
        self.co_user_password = "1234"

        self.user_name_label = tk.Label(self, text="Enter User Name : ")
        self.user_name_label.pack()

        self.user_name_entry = tk.Entry(self)
        self.user_name_entry.pack()


        self.user_password_label = tk.Label(self, text="Enter User password : ")
        self.user_password_label.pack()

        self.user_password_entry = tk.Entry(self)
        self.user_password_entry.pack()

        self.login_button = tk.Button(self, text = "Login", command = self.check_login)
        self.login_button.pack()


    def check_login(self):
        name = self.user_name_entry.get()
        password = self.user_password_entry.get()

        if name == "" or password == "" :
            messagebox.showwarning("Warning", "Empty Field")
        elif name == self.co_user_name and password == self.co_user_password :
            messagebox.showinfo("You Logined In", "Everything Is Good")
        else:
            messagebox.showerror("Error","Wrong User Name of Password ")



class App(tk.Tk) :
    def __init__(self):
        super().__init__()

        self.title("SSS")
        self.geometry("500x500")


        login = LoginPage(parent=self) 
        login.pack(pady = 0)     


if __name__ =="__main__" :
    app = App()
    app.mainloop()