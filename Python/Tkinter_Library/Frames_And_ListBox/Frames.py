import tkinter as tk

class my_custom_frame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)


        label = tk.Label(self, text="This Is My Custom Frame")
        label.pack()

        button = tk.Button(self,text="Click Me")
        button.pack()

    

root = tk.Tk()

my_frame = my_custom_frame(root)
my_frame.pack()

root.mainloop()



