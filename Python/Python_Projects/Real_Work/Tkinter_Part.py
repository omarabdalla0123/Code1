import tkinter as tk
from tkinter import messagebox


class Login_Screen(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.co_password = "1234"

        self.password_label = tk.Label(self, text="Enter Password : ")
        self.password_label.pack()

        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        self.submit_button = tk.Button(self, text = "Submit", command = self.check_password)


    def check_password(self):
        if self.password == "":
            messagebox.showwarning("Warning","Empty Field")
        elif self.password == self.co_password :
            messagebox.showinfo("Correct Password", "You Entered The Correct Password")
        else:
            messagebox.showerror("Error", "Wrong Password")




class App(tk.Tk):
    def __init__(self) :
        super().__init__()

        self.title("Market App")
        self.geometry("500x500")
        self.resizable(False,False)



        login = Login_Screen(parent=self)
        login.pack()


if __name__ == "__name__":
    app = App()
    app.mainloop()

# conn.close()