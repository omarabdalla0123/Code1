import tkinter as tk
from tkinter import font

def create_calculator():
    # Create main window
    root = tk.Tk()
    root.title("Python Calculator")
    root.resizable(False, False)
    
    # Create display screen
    display_font = font.Font(size=20)
    display = tk.Entry(root, font=display_font, justify='right', bd=10, relief=tk.RIDGE)
    display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
    
    # Button click functions
    def button_click(number):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current + str(number))
    
    def clear_display():
        display.delete(0, tk.END)
    
    def calculate():
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    
    def backspace():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])
    
    # Calculator buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]
    
    # Create buttons
    for (text, row, col) in buttons:
        if text == '=':
            btn = tk.Button(root, text=text, font=font.Font(size=14), 
                           command=calculate, bg='orange', fg='white', height=2, width=5)
        elif text in ['C', '⌫']:
            btn = tk.Button(root, text=text, font=font.Font(size=14), 
                           command=clear_display if text == 'C' else backspace, 
                           bg='lightgray', height=2, width=5)
        else:
            btn = tk.Button(root, text=text, font=font.Font(size=14), 
                           command=lambda t=text: button_click(t), 
                           height=2, width=5)
        btn.grid(row=row, column=col, padx=2, pady=2)
    
    # Additional buttons
    clear_btn = tk.Button(root, text='C', font=font.Font(size=14), 
                         command=clear_display, bg='red', fg='white', height=2, width=5)
    clear_btn.grid(row=5, column=0, padx=2, pady=2)
    
    backspace_btn = tk.Button(root, text='⌫', font=font.Font(size=14), 
                             command=backspace, bg='lightgray', height=2, width=5)
    backspace_btn.grid(row=5, column=1, padx=2, pady=2)
    
    # Run the application
    root.mainloop()

# Start the calculator
create_calculator()