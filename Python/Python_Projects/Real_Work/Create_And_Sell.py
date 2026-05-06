import tkinter as tk
from tkinter import messagebox

class Login_Page(tk.Frame) :
    def __init__(self,parent):
        super().__init__(parent)

        self.co_password = "1234"

        self.password_label = tk.Label(self,text="Enter The Password : ")
        self.password_label.pack()

        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        self.submit_button = tk.Button(self, text = "Submit", command = self.check_password )

    def check_password(self):
        password = self.password_entry.get()
        if password == "":
            messagebox.showwarning("Warning","Empty Field")
        elif password == self.co_password :
            messagebox.showinfo("Correct Password", "You Put The Correct Password")
        else:
            messagebox.showerror("Error","Wrong Password")


class Sell_Page(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.items_list = tk.Listbox(self)
        self.items_list.pack()

        sell_button = tk.Button(self, text="Sell")
        sell_button.pack()



class Create_Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.create_label = tk.Label(self,text="Enter The Item Name : ")
        self.create_label.pack()

        self.create_entry = tk.Entry(self)
        self.create_entry.pack()

        self.create_button = tk.Button(self, text = "Create", command = self.check_password )


    # def create_item(self) :

    #     item = self.create_entry.get()
    #     if item == "":
    #         messagebox.showwarning("Warning","Empty Field")
    #     else:
    #         items_list

class App(tk.Tk) :
    def __init__(self):
        super().__init__()

        self.title("My Market")
        self.geometry("500x500")
        self.resizable(False,False)

    
        container = tk.Frame(self)
        container.pack(side="top",fill = "both", expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}


        for F in (Login_Page, Sell_Page):
            frame = F(container) 
            self.frames[F.__name__] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")


        
        





if __name__ =="__main__":
    app = App()
    app.mainloop()
