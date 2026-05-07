import tkinter as tk

class Container(tk.Tk):
    def __init__(self) :
        super().__init__()

        self.title("My App")
        self.geometry("500x500")


        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight =1)
        container.grid_columnconfigure(0, weight =1)

        self.frames = {}

        for PageClass in (Page1, Page2):
            frame = PageClass(container, self)
            self.frame[PageClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")







class Page1(tk.Frame):
    def __init__(self, paretnt, controller):
        super().__init__(paretnt)
        self.controller = controller

        label = tk.Label(self)
        label.pack()

        button = tk.Button(self,text="Go To Page 2", command= lambda : controller.show_frame("Page2") )
        button.pack()

        self.show_frame("Page1")

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()



class Page2(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self,text="Page 2")
        label.pack()

        button = tk.Button(self,text = "Go to Page 1", command = controller.show_frame("Page1"))
        button.pack()

if __name__ == "__main__":
    app = Container()
    app.mainloop