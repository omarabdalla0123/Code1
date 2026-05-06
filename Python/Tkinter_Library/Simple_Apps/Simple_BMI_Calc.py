import tkinter as tk



def ca():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    height_m = height / 100
    res = weight / (height_m)**2
    if res <= 18.5 :
        res_label.config(text = f"BMI : {res} Underweight")
    elif res >= 18.5 and res <= 24.9:
        res_label.config(text = f"BMI : {res} Normal")
    elif res >= 25 and res <= 29.9 :
        res_label.config(text = f"BMI : {res} Overweight")
    elif res >= 30 :
        res_label.config(text = f"BMI : {res} Obese")    
    else: 
        res_label.config(text = "please put numbers only")

root =  tk.Tk()
root.title("Simple BMI Calc")
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg = "#FFFFFF")

weight_label = tk.Label(root, text = "Enter Your Weight in Kg :")
weight_label.pack()

weight_entry =  tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text = "Enter Your height in Cm :")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()


calc = tk.Button(root, text = "Calculate", command = ca)
calc.pack()

res_label = tk.Label(root, text = "")
res_label.pack()


root.mainloop()