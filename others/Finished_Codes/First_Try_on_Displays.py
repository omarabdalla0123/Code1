import tkinter as tk 
def create_calculator() :

     
    def button_click(number):
        current = length_display.get() + width_display.get()
        Delete= length_display.delete(0,tk.END)
        length_display.insert(0,current + str(number))



    def clear_display():
        length_display.delete(0,tk.END)




    def calculate() :
        try :
            result = eval(length_display.get()+ width_display.get())
            length_display.delete(0, tk.END)
            length_display.insert(0,str(result))
        except: 

            length_display.delete(0, tk.END)
            length_display.insert(0, str("Error"))   

    def backspace():
        current = length_display.get()
        length_display.delete(0,tk.END)
        length_display.insert(0,current[:-1])
     
   
     
     
     
    root = tk.Tk()

    root.title('Dispaly Checks')
    root.geometry("700x700")

    root.resizable(False, False)

    length_label = tk.Label(root, text="Length", font=('Arial', 18, 'bold'))
    length_label.grid(row=0, column=0)

    result_label = tk.Label(root, text="Result", font=('Arial', 18, 'bold'))
    result_label.grid(row=2, column=0)

    length_display = tk.Entry(root, font=('Arial', 17))
    length_display.grid(row=0, column=1)

    width_label = tk.Label(root, text="Width", font=('Arial', 18, 'bold'))
    width_label.grid(row=1, column=0)

    width_display = tk.Entry(root, font=('Arial', 17))
    width_display.grid(row=1, column=1)

    result_display = tk.Entry(root, font=('Arial', 17))
    result_display.grid(row=2, column=1)

    buttons = [
        ('1', 0, 3), ('2', 0, 4), ('3', 0, 5),
        ('4', 1, 3), ('5', 1, 4), ('6', 1, 5),
        ('7', 2, 3), ('8', 2, 4), ('9', 2, 5),
        ('C', 3, 3), ('0', 3, 4), ('=', 3, 5),
        ('-', 0, 6), ('+', 1,6 ), ('*', 2, 6),
        ('/', 3, 6)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            btn = tk.Button(root, text=text, command=calculate, fg='Green', bg='blue', height=2, width=5)
        elif text in ['C', '⌫']:
            btn = tk.Button(root, command=clear_display, text=text if text == 'C' else backspace, height=2, width=5)
        else:
            btn = tk.Button(root, text=text, command=lambda t=text: button_click(t), height=2, width=5)

        btn.grid(row=row, column=col, pady=2, padx=2)

    root.mainloop()







create_calculator()
