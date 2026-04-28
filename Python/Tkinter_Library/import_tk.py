import tkinter as tk 



def click() :
    print("Button Clicked!")



def get_text() :
    user = entry.get()
    print(f"You typed : {user}.") 


def greet():
    name = entry.get()
    label.config(text = f"Hello {name}")

window = tk.Tk()


window.title("My First App")

window.geometry("500x500")

label = tk.Label(window, text = "Hello World !")
label.pack()



button = tk.Button(window, text = "First Button", command = get_text)
button.pack()


button1 = tk.Button(window, text = "greet Button", command = greet)
button1.pack()

entry = tk.Entry(window)
entry.pack()

window.mainloop()