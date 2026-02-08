import tkinter as tk 
class GUI :

    
    def __init__(self) :
    
        def Number_one():
            self.basic.lengthtextbox.insert(tk.END,"Button was clicked!\n")

        self.basic = tk.Tk()
       
        self.basic.geometry("600x600")
        self.basic.title("Area_calculator")

        self.basic.equal = tk.Button(self.basic, text="=")
        self.basic.equal.place(x=200, y=200, width=50, height=50)
      


        self.basic.lengthtextbox = tk.Text(self.basic, font=('Arial', 18), width=40, height=3)
        self.basic.lengthtextbox.pack(padx=20,pady=20)




       
        self.basic.buttonframe = tk.Frame(self.basic)
        self.basic.buttonframe.columnconfigure(0, weight=1, uniform="button_cols")
        self.basic.buttonframe.columnconfigure(1, weight=1, uniform="button_cols")
        self.basic.buttonframe.columnconfigure(2, weight=1, uniform="button_cols")

        # Configure rows to have the same height (optional)
        self.basic.buttonframe.rowconfigure(0, weight=1, uniform="button_rows")
        self.basic.buttonframe.rowconfigure(1, weight=1, uniform="button_rows")
        self.basic.buttonframe.rowconfigure(2, weight=1, uniform="button_rows")
        self.basic.buttonframe.rowconfigure(3, weight=1, uniform="button_rows")
    # Bottom spacer
        #Numbers
        btn0 = tk.Button(self.basic.buttonframe, text=0, font=('Arial', 18))
        btn0.grid(row=3, column=1, sticky="nsew")  # Changed to nsew

        btn1 = tk.Button(self.basic.buttonframe, text=1, font=('Arial', 18))
        btn1.config(command=Number_one)
        btn1.grid(row=0, column=0, sticky="nsew")  # Changed to nsew

        btn2 = tk.Button(self.basic.buttonframe, text=2, font=('Arial', 18))
        btn2.grid(row=0, column=1, sticky="nsew")  # Changed to nsew

        btn3 = tk.Button(self.basic.buttonframe, text=3, font=('Arial', 18))
        btn3.grid(row=0, column=2, sticky="nsew")  # Changed to nsew

        btn4 = tk.Button(self.basic.buttonframe, text=4, font=('Arial', 18))
        btn4.grid(row=1, column=0, sticky="nsew")  # Changed to nsew

        btn5 = tk.Button(self.basic.buttonframe, text=5, font=('Arial', 18))
        btn5.grid(row=1, column=1, sticky="nsew")  # Changed to nsew

        btn6 = tk.Button(self.basic.buttonframe, text=6, font=('Arial', 18))
        btn6.grid(row=1, column=2, sticky="nsew")  # Changed to nsew

        btn7 = tk.Button(self.basic.buttonframe, text=7, font=('Arial', 18))
        btn7.grid(row=2, column=0, sticky="nsew")  # Changed to nsew

        btn8 = tk.Button(self.basic.buttonframe, text=8, font=('Arial', 18))
        btn8.grid(row=2, column=1, sticky="nsew")  # Changed to nsew

        btn9 = tk.Button(self.basic.buttonframe, text=9, font=('Arial', 18))
        btn9.grid(row=2, column=2, sticky="nsew")  # Changed to nsew

        btnC = tk.Button(self.basic.buttonframe, text="C", font=('Arial', 18))
        btnC.grid(row=3, column=0, sticky="nsew")  # Changed to nsew

        btnDelete = tk.Button(self.basic.buttonframe, text="Delete", font=('Arial', 18))
        btnDelete.grid(row=3, column=2, sticky="nsew")  # Changed t


        self.basic.buttonframe.pack(fill='x')





        self.basic.mainloop()

GUI()
