import tkinter as tk

def create_calculator():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Room Area Calculator")

    # Variables to track widget choice
    length_choice = tk.StringVar(value="entry")
    width_choice = tk.StringVar(value="entry")

    # --- Length Widgets ---
    tk.Label(root, text="Length:").grid(row=0, column=0, sticky='w')
    length_entry = tk.Entry(root, font=('Arial', 14))
    length_entry.grid(row=0, column=1, columnspan=2, sticky='ew')
    length_text = tk.Text(root, font=('Arial', 14), height=1, width=10)
    length_text.grid(row=0, column=1, columnspan=2, sticky='ew')
    length_text.grid_remove()  # Hide initially

    # --- Width Widgets ---
    tk.Label(root, text="Width:").grid(row=1, column=0, sticky='w')
    width_entry = tk.Entry(root, font=('Arial', 14))
    width_entry.grid(row=1, column=1, columnspan=2, sticky='ew')
    width_text = tk.Text(root, font=('Arial', 14), height=1, width=10)
    width_text.grid(row=1, column=1, columnspan=2, sticky='ew')
    width_text.grid_remove()  # Hide initially

    # --- Result Display ---
    tk.Label(root, text="Result:").grid(row=2, column=0, sticky='w')
    result_display = tk.Entry(root, font=('Arial', 14), state='readonly')
    result_display.grid(row=2, column=1, columnspan=2, sticky='ew')

    # --- Radio Buttons for Length ---
    tk.Radiobutton(root, text="Entry", variable=length_choice, value="entry",
                   command=lambda: switch_widget(length_choice, length_entry, length_text)).grid(row=0, column=3)
    tk.Radiobutton(root, text="Text", variable=length_choice, value="text",
                   command=lambda: switch_widget(length_choice, length_entry, length_text)).grid(row=0, column=4)

    # --- Radio Buttons for Width ---
    tk.Radiobutton(root, text="Entry", variable=width_choice, value="entry",
                   command=lambda: switch_widget(width_choice, width_entry, width_text)).grid(row=1, column=3)
    tk.Radiobutton(root, text="Text", variable=width_choice, value="text",
                   command=lambda: switch_widget(width_choice, width_entry, width_text)).grid(row=1, column=4)

    # --- Button click logic ---
    def button_click(number):
        # Insert number into the selected length or width widget
        if focus_var.get() == "length":
            if length_choice.get() == "entry":
                length_entry.insert(tk.END, str(number))
            else:
                length_text.insert(tk.END, str(number))
        elif focus_var.get() == "width":
            if width_choice.get() == "entry":
                width_entry.insert(tk.END, str(number))
            else:
                width_text.insert(tk.END, str(number))

    # --- Focus selection (which field to enter numbers into) ---
    focus_var = tk.StringVar(value="length")
    tk.Radiobutton(root, text="Length", variable=focus_var, value="length").grid(row=3, column=1)
    tk.Radiobutton(root, text="Width", variable=focus_var, value="width").grid(row=3, column=2)

    # --- Calculate area ---
    def calculate():
        if length_choice.get() == "entry":
            l = length_entry.get()
        else:
            l = length_text.get("1.0", tk.END).strip()
        if width_choice.get() == "entry":
            w = width_entry.get()
        else:
            w = width_text.get("1.0", tk.END).strip()
        try:
            area = float(l) * float(w)
            result_display.config(state='normal')
            result_display.delete(0, tk.END)
            result_display.insert(0, str(area))
            result_display.config(state='readonly')
        except:
            result_display.config(state='normal')
            result_display.delete(0, tk.END)
            result_display.insert(0, "Error")
            result_display.config(state='readonly')

    # --- Switch widgets based on radio selection ---
    def switch_widget(choice_var, entry_widget, text_widget):
        if choice_var.get() == "entry":
            entry_widget.grid()
            text_widget.grid_remove()
        else:
            text_widget.grid()
            entry_widget.grid_remove()

    # --- Calculator buttons (0-9 and .) ---
    buttons = [
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
        ('4', 5, 0), ('5', 5, 1), ('6', 5, 2),
        ('1', 6, 0), ('2', 6, 1), ('3', 6, 2),
        ('0', 7, 1), ('.', 7, 0)
    ]
    for (text, row, col) in buttons:
        tk.Button(root, text=text, width=5, height=2,
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=2, pady=2)

    # --- Calculate button ---
    tk.Button(root, text="Calculate", width=12, height=2, command=calculate).grid(row=7, column=2, columnspan=2, padx=2, pady=2)

    root.mainloop()

create_calculator()