import tkinter as tk



def add():
    first_num = int(entry.get())
    second_num = int(entry1.get())

    res = first_num + second_num 
    label2.config(text = f"Result : {res}")

def substract():
    first_num = int(entry.get())
    second_num = int(entry1.get())

    res = first_num - second_num 
    label2.config(text = f"Result : {res}")



root = tk.Tk()

root.title("Simple Calc")
root.geometry("500x500")

label = tk.Label(root, text ="First Number")
label.place(x= 50, y = 80)
entry = tk.Entry(root)
entry.place(x= 190, y = 80)







label1 = tk.Label(root, text ="Second Number")
label1.place(x= 50, y = 110)
entry1 = tk.Entry(root)
entry1.place(x= 190, y = 110)


button = tk.Button(root, text ="Add", command = add)
button.place(x= 280, y = 135)

button1 = tk.Button(root, text ="Subtract", command = substract)
button1.place(x= 200, y = 135)




label2 = tk.Label(root, text ="Result :  ")
label2.place(x= 220, y = 50)






root.mainloop()