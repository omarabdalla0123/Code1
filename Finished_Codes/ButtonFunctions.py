import tkinter as tk
from tkinter import messagebox

class Gui :
    def __init__(self) :

        self.plat = tk.Tk()
        # menu
        self.menubar = tk.Menu(self.plat,)
        self.firstmenu = tk.Menu(self.menubar, tearoff=0)
        self.firstmenu.add_command(label="close", command=self.on_closing)
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label = "show message", command=self.show_message)

        self.menubar.add_cascade(menu=self.firstmenu, label="First", font=('Arial', 19))
        self.menubar.add_cascade(menu=self.actionmenu, label="Second")

        self.plat.config(menu=self.menubar)
    
        self.label = tk.Label(self.plat, text="your message", font=('Arial', 15) )
        self.label.pack()
        
        self.textbox = tk.Text(self.plat, font=('Arial', 16))
        self.textbox.bind("<Key>", self.shortcut)
        self.textbox.pack()

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.plat, text="Show a MessageBox", font=('Arial', 15), variable=self.check_state)
        self.check.pack()

        self.button = tk.Button(self.plat, text="Click Me", font=('Arial', 15), command=self.show_message)
        self.button.pack()

        self.clearbtn = tk.Button(self.plat, text="Clear", font=('Arial', 15), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)


        self.plat.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.plat.mainloop()

    def show_message(self) :
          
           if self.check_state.get() == 0 :
   
                print(self.textbox.get('1.0', tk.END))
           else:
               messagebox.showinfo(title="Click Me Message",message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event) :     
         
     if event.state == 12 and event.keysym == "Return" :
       self.show_message()  
       
    def on_closing(self) :
     if messagebox.askyesno(title="Quit ?", message="do you really want to quit ?") :
         
      self.plat.destroy()

    def clear(self) :
       self.textbox.delete('1.0', tk.END)




Gui()  




        