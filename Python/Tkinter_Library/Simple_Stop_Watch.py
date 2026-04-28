import tkinter as tk
from PIL import Image , ImageTk

def count():
    count_label.config(text=count)
    count_label.after(1000, count)
   


def stop():
    count_label.config(text = count)



root =  tk.Tk()
root.title("Simple Stop Watch")
root.geometry("500x500")
root.resizable(False,False)
root.config(bg = "white")

# image = Image.open(".png")
# image = image.size((500,500))
# bg = ImageTk.PhotoImage(image)

count_label = tk.Label(root, text= "0")
count_label.place(x=155,y=20)


start_button = tk.Button(root, text = "Start", command = count)
start_button.place(x=100, y=100)



stop_button = tk.Button(root, text = "Stop", command = stop)
stop_button.place(x=190, y=100)






root.mainloop()