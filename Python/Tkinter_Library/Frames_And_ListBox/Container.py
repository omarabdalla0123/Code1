import tkinter as tk

class Container(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("My App")
        self.geometry("500x500")

        
        container = tk.Frame(self)
        container.pack(side = "top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

      ##  for PageClass in (Page1, Page2):
        #     frame = PageClass(container, self)
        #     self.frames[PageClass.__name__] = frame
        #     frame.grid(row= 0, column = 0, sticky = "nsew")

        # self.show_frame("Page")