import tkinter as tk 
from tkinter import messagebox




def ca():
    if weight_entry.get() == "" or height_entry.get() == "":
        messagebox.showerror("Error", "Please enter your weight and height!")
        return
    
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    height_m = height / 100
    res = weight / (height_m)**2
    
    if res <= 18.5:
        messagebox.showinfo("Result", f"BMI: {res:.1f} - Underweight")
    elif res >= 18.5 and res <= 24.9:
        messagebox.showinfo("Result", f"BMI: {res:.1f} - Normal")
    elif res >= 25 and res <= 29.9:
        messagebox.showinfo("Result", f"BMI: {res:.1f} - Overweight")
    elif res >= 30:
        messagebox.showinfo("Result", f"BMI: {res:.1f} - Obese")


root = tk.Tk()

root.geometry("500x500")
root.resizable(False,False)
root.title("Message Box")
root.config(bg = "#FFFFFF")
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\Photos\torn.ico")


#messagebox.askyesno("Success", "Password generated")

weight_entry = tk.Entry(root)
weight_entry.pack()


height_entry = tk.Entry(root)
height_entry.pack()


button = tk.Button(root, text="Generate", command = ca)
button.pack()


root.mainloop()