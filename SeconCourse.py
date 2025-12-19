
import tkinter as tk
from PIL import Image, ImageTk  # Correct import statement
window = tk.Tk()


window.geometry("500x500") #to customize the size of the window
window.title("Second Start")
try:
    # Open the image using PIL
    image = Image.open('unnamed.png')
    # Convert to PhotoImage for Tkinter
    icon = ImageTk.PhotoImage(image)
    window.iconphoto(True, icon)
except Exception as e:
    print(f"Could not load icon: {e}")


window.label = tk.Label(window,text="Your Message", font=('Arial', 24, 'bold'), fg='#00ff00',bg="black",  bd=10)


window.label.pack()

#window.label.place(x=0, y=0)

def click() :
    print("hello")
window.button.config()
window.button.config(command=click)

window.textbox = tk.Text(window, font=('Arial', 15))
window.textbox.pack()

window.mainloop()