import tkinter as tk

def create_calculator():

    def button_click(number):
        current = display.get()
        display.delete(0,tk.END)
        display.insert(0,current + str(number))



    def clear_display():
        display.delete(0,tk.END)




    def calculate() :
        try :
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0,str(result))
        except: 

            display.delete(0, tk.END)
            display.insert(0, str("Error"))   

    def backspace():
        current = display.get()
        display.delete(0,tk.END)
        display.insert(0,current[:-1])


    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(False,False) # stop expending the size so it will be only by geometry size  

    

    display = tk.Entry(root,font=('Arial',20),justify='right', bd=10, relief=tk.RIDGE, fg="#000000", bg="#FFFFFF") 
    display.config()
    display.grid(row=0, column=0,  columnspan=4 ,sticky='nsew', padx=5, pady=5 )







    """
    textbox = tk.Text(root)
    textbox.grid()

    """





    buttons = [
        ('1', 1, 0) , ('2', 1, 1) , ('3', 1, 2),
        ('4', 2, 0) , ('5', 2, 1) , ('6', 2, 2),
        ('7', 3, 0) , ('8', 3, 1) , ('9', 3, 2),
        ('C', 4, 0) , ('0', 4, 1) , ('=', 4, 2),
        ('-', 1, 3) , ('+', 2, 3) , ('*', 3, 3),
        ('/', 4, 3)
    ]


    for (text,row,col) in buttons :
        if text =='=' :
            btn = tk.Button(root, text=text , command= calculate , fg='Green', bg='blue',height=2, width=5)
        elif text in ['C', '⌫']:
            btn = tk.Button(root,command = clear_display, text=text if text =='C' else backspace , height=2, width=5)

        else:
            btn = tk.Button(root, text=text, command = lambda t=text: button_click(t), height=2, width=5)

        btn.grid( row=row, column=col, pady= 2, padx = 2)
    root.mainloop()
create_calculator()