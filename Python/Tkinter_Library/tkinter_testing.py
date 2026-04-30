import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Sudan George Kordahi")
root.geometry("600x400")
root.resizable(False, False)
image =  Image.open(r"D:\Code\Python\Tkinter_Library\bg.png")
image = image.resize((600, 400))
photo = ImageTk.PhotoImage(image)
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\torn.ico")


root.mainloop()