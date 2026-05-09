import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Store Management System")
        self.geometry("500x500")

        # 1. Centralized Data Storage
        self.inventory_data = []

        # 2. The Container
        # This frame holds all our "forms" in one spot
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # 3. Create every form class and stack them
        for F in (Login_Page, Home_Page, Selling_Page, Items_And_Stock):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            # Stack all frames in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        # Start on the Login Form
        self.show_form("Login_Page")

    def show_form(self, page_name):
        """Brings the requested form to the front."""
        frame = self.frames[page_name]
        frame.tkraise()

    def add_item_to_master_list(self, item_name):
        """Adds data to the brain and updates the Selling Page Form."""
        self.inventory_data.append(item_name)
        # Update the listbox on the Selling_Page form specifically
        self.frames["Selling_Page"].update_listbox(self.inventory_data)

class Login_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="LOGIN FORM", font=("Arial", 14, "bold")).pack(pady=20)
        tk.Label(self, text="Password:").pack()
        self.pass_entry = tk.Entry(self, show="*")
        self.pass_entry.pack(pady=5)

        tk.Button(self, text="Enter", width=15, 
                  command=self.login_check).pack(pady=20)

    def login_check(self):
        if self.pass_entry.get() == "1234":
            self.controller.show_form("Home_Page")
        else:
            messagebox.showerror("Error", "Invalid Password")

class Home_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="HOME FORM", font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(self, text="Go to Selling Page", width=20,
                  command=lambda: controller.show_form("Selling_Page")).pack(pady=10)
        
        tk.Button(self, text="Go to Add Items Form", width=20,
                  command=lambda: controller.show_form("Items_And_Stock")).pack(pady=10)
        
        tk.Button(self, text="Logout", width=20,
                  command=lambda: controller.show_form("Login_Page")).pack(pady=10)

class Selling_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="SELLING FORM (Inventory)", font=("Arial", 12)).pack(pady=10)
        
        self.listbox = tk.Listbox(self, width=40)
        self.listbox.pack(pady=10)

        tk.Button(self, text="Back Home", 
                  command=lambda: controller.show_form("Home_Page")).pack()

    def update_listbox(self, data):
        """Updates the listbox whenever the master data changes."""
        self.listbox.delete(0, tk.END)
        for item in data:
            self.listbox.insert(tk.END, item)

class Items_And_Stock(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="ADD ITEM FORM", font=("Arial", 12)).pack(pady=10)
        
        tk.Label(self, text="Item Name:").pack()
        self.item_name = tk.Entry(self)
        self.item_name.pack(pady=5)

        tk.Button(self, text="Save to Inventory", 
                  command=self.save_data).pack(pady=10)
        
        tk.Button(self, text="Back Home", 
                  command=lambda: controller.show_form("Home_Page")).pack()

    def save_data(self):
        item = self.item_name.get()
        if item:
            # Send the data to the App class
            self.controller.add_item_to_master_list(item)
            self.item_name.delete(0, tk.END)
            messagebox.showinfo("Saved", f"{item} added to stock!")
        else:
            messagebox.showwarning("Empty", "Please enter an item name")

if __name__ == "__main__":
    app = App()
    app.mainloop()