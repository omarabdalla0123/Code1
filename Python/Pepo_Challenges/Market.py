import tkinter as tk
from tkinter import messagebox



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Store Management System")
        self.geometry("500x500")

        self.inventory_data = []

        container = tk.Frame(self)
        container.pack(side="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)


        self.frames = {}

        for F in (Login_Page,Home_Page,Selling_Page,Stock_Page):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame

            frame.grid(column = 0, row = 0, sticky="nsew")
        
        self.show_form("Login_Page")



    def show_form(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



    def add_item_to_master_list(self, item_name):
        self.inventory_data.append(item_name)
        self.frames["Selling_Page"].update_listbox(self.inventory_data)







class Login_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self,text = "Enter Your Password : ").pack()

        self.password_entry = tk.Entry(self, show = "*")
        self.password_entry.pack()


        tk.Button(self, text = "Login", command = self.check_password).pack()


    def check_password(self):
        if self.password_entry.get() == "1234" :
            messagebox.showinfo("Correct", "You Entered The Corrrect Password ")
            self.controller.show_form("Home_Page")
        else:
            messagebox.showwarning("Warning", "Your Password Is Wrong ")
            







class Home_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        tk.Label(self, text = "! Home Page !").pack()

        tk.Button(self, text="Selling Page", command=lambda: controller.show_form("Selling_Page")).pack()
        tk.Button(self, text="Stock Page",   command=lambda: controller.show_form("Stock_Page")).pack()


        tk.Button(self, text = "Logout", command = lambda : controller.show_form("Login_Page")).pack()





class Selling_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller


        tk.Label(self, text = "List Box").pack()

        self.listbox = tk.Listbox(self)
        self.listbox.pack()


        tk.Button(self, text = "Back Home Page", command = lambda : controller.show_form("Home_Page")).pack()

    def update_listbox(self, data):
        self.listbox.delete(0, tk.END)
        for item in data:
            self.listbox.insert(tk.END, item)




class Stock_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text = "Add Item Name : ").pack()

        self.item_entry = tk.Entry(self)
        self.item_entry.pack()

        tk.Button(self, text="Save To ListBox", command=self.save_data).pack()

        tk.Button(self, text = "Home Page", command = lambda : controller.show_form("Home_Page")).pack()

    def save_data(self):
        item = self.item_entry.get()
        if item :
            self.controller.add_item_to_master_list(item)
            self.item_entry.delete(0, tk.END)
            messagebox.showinfo("Saved", f"{item} added to stock!")
        else:
            messagebox.showwarning("Empty", "Please enter an item name")



if __name__ == "__main__":
    app = App()

    app.mainloop()