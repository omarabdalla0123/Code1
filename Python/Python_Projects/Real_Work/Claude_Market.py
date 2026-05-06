import tkinter as tk
from tkinter import messagebox


class Login_Screen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.co_password = "1234"

        self.password_label = tk.Label(self, text="Enter Password : ")
        self.password_label.pack()

        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.check_password)
        self.submit_button.pack()

    def check_password(self):
        if self.password_entry.get() == "":
            messagebox.showwarning("Warning", "Empty Field")
        elif self.password_entry.get() == self.co_password:
            messagebox.showinfo("Correct Password", "You Entered The Correct Password")
        else:
            messagebox.showerror("Error", "Wrong Password")


class Sell_Screen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Add a title label
        title_label = tk.Label(self, text="Items List", font=("Arial", 12, "bold"))
        title_label.pack()

        # Create listbox
        self.items_list = tk.Listbox(self, height=15, width=40)
        self.items_list.pack(pady=10)

        # Add some sample items to the listbox
        self.items = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Grapes"]
        for item in self.items:
            self.items_list.insert(tk.END, item)

        # Add button frame for better organization
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Sell button
        sell_button = tk.Button(button_frame, text="Sell", bg="green", fg="white", width=15)
        sell_button.pack(side=tk.LEFT, padx=5)

        # Delete button (optional - to remove selected item)
        delete_button = tk.Button(button_frame, text="Delete Item", bg="red", fg="white", width=15, command=self.delete_item)
        delete_button.pack(side=tk.LEFT, padx=5)

    def delete_item(self):
        """Delete selected item from listbox"""
        selected = self.items_list.curselection()
        if selected:
            self.items_list.delete(selected)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Market App")
        self.geometry("500x500")
        self.resizable(False, False)

        # Create a container frame to hold all pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to store all frames
        self.frames = {}

        # Create all frames
        for F in (Login_Screen, Sell_Screen):
            frame = F(container)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the login screen by default
        self.show_frame("Login_Screen")

        # Create menubar
        home_menubar = tk.Menu(self)
        self.config(menu=home_menubar)

        # Create Pages menu
        pages_menu = tk.Menu(home_menubar, tearoff=0)
        home_menubar.add_cascade(label="Pages", menu=pages_menu)

        # Add menu items to switch between frames
        pages_menu.add_command(label="Login", command=lambda: self.show_frame("Login_Screen"))
        pages_menu.add_command(label="Sell", command=lambda: self.show_frame("Sell_Screen"))
        pages_menu.add_separator()
        pages_menu.add_command(label="Exit", command=self.quit)

    def show_frame(self, context):
        """Show the specified frame"""
        frame = self.frames[context]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()