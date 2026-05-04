import tkinter as tk 
from tkinter import messagebox
## Student System

class LoginScreen(tk.Frame) :


    def __init__(self, parent):
        super().__init__(parent)
        
        self.co_user_name = "omer"
        self.co_user_password = "1234"

        tk.Label(self, text = "Put User Name :").pack()
        self.user_name = tk.Entry(self)
        self.user_name.pack()
        tk.Label(self,text= "Put Password :").pack()
        self.user_password = tk.Entry(self)
        self. user_password.pack()

        tk.Button(self, text= "Login", command = self.check_login).pack()


    def check_login(self):
        name = self.user_name.get()
        password = self.user_password.get()

        if name == "" and password == "":
            messagebox.showwarning("Warning", "Empty Field")
        elif name == self.co_user_name and password == self.co_user_password :
            messagebox.showinfo("Welcome", "Everything Is Okay Now")
        else:
            messagebox.showerror("Error", "Wrong UserName or Password")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student System")
        self.geometry("500x500")


        login = LoginScreen(parent=self)
        login.pack(pady =0)


if __name__ == "__main__" :
    app = App()
    app.mainloop()






