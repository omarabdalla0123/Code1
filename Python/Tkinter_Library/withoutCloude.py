import tkinter as tk


class LoginPage :

    def __init__(self,parent):
        super().__init__(parent)

        self.co_user_name_label = tk.Label(self, text="Enter User Name : ")
        self.co_user_name_label.pack()

        self.co_user_name_entry = tk.Entry(self)
        self.co_user_name_entry.pack()


        self.co_user_password_label = tk.Label(self, text="Enter User password : ")
        self.co_user_password_label.pack()

        self.co_user_password_entry = tk.Label(self)
        self.co_user_password_entry.pack()