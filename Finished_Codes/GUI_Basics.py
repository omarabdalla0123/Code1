import tkinter as tk
from PIL import Image, ImageTk 



plat = tk.Tk()
plat.title("GUI")
plat.geometry("500x500")
text = ""


try:
    # Open the image using PIL
    image = Image.open('unnamed.png')
    # Convert to PhotoImage for Tkinter
    icon = ImageTk.PhotoImage(image)
    plat.iconphoto(True, icon)
except Exception as e:
    print(f"Could not load icon: {e}")

label = tk.Label(plat, text ="Calculator" , font = ('Arial' , 18))
label.pack(padx=20, pady=20)


textbox = tk.Text(plat, height=3, font=('Arial' , 16))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(plat)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)
buttonframe.columnconfigure(4,weight=1)
buttonframe.columnconfigure(5,weight=1)
buttonframe.columnconfigure(6,weight=1)
buttonframe.columnconfigure(7,weight=1)
buttonframe.columnconfigure(8,weight=1)
buttonframe.columnconfigure(9,weight=1)
buttonframe.columnconfigure(10,weight=1)
buttonframe.columnconfigure(11,weight=1)
buttonframe.columnconfigure(12,weight=1)
buttonframe.columnconfigure(13,weight=1)
buttonframe.columnconfigure(14,weight=1)
buttonframe.columnconfigure(15,weight=1)
#numbers
btn0 = tk.Button(buttonframe, text=0 , font=('Arial', 18))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text=1 , font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text=2 , font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text=3 , font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E,)

btn4 = tk.Button(buttonframe, text=4 , font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text=5 , font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text=6 , font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text=7 , font=('Arial', 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text=8 , font=('Arial', 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text=9 , font=('Arial', 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
#clear and delete
btnc = tk.Button(buttonframe, text="C" , font=('Arial', 18))
btnc.grid(row=3, column=0, sticky=tk.W+tk.E)

btndelete = tk.Button(buttonframe, text="Delete", font=('Arial', 18))
btndelete.grid(row=3, column=2, sticky=tk.W+tk.E)
#operations
btnminues= tk.Button(buttonframe, text="-" , font=('Arial', 18))
btnminues.grid(row=0, column=3, sticky=tk.W+tk.E)

btnplus= tk.Button(buttonframe, text="+" , font=('Arial', 18))
btnplus.grid(row=1, column=3, sticky=tk.W+tk.E)

btnmulty= tk.Button(buttonframe, text="*" , font=('Arial', 18))
btnmulty.grid(row=2, column=3, sticky=tk.W+tk.E)

btndevi= tk.Button(buttonframe, text="/" , font=('Arial', 18))
btndevi.grid(row=3, column=3, sticky=tk.W+tk.E)
# =
btnequal= tk.Button(buttonframe, text="=" , font=('Arial', 18))
btnequal.grid(row=4, column=0, sticky=tk.W+tk.E )


buttonframe.pack(fill='x')

#password = tk.Entry(plat)
#password.pack(padx=20, pady=20)
""""""
button =tk.Button(plat, text="Click" , font=('Arial', 12))
button.pack(pady=100)
"""
testbutton = tk.Button(plat, text="Test" , font=('Arial', 12))
#testbutton.place(x=65, y=358, height=40 , width=62 )
testbutton.place( y=358, height=40 , width=246 )

"""




"""

plat.menu = tk.Menu(plat, menu="First", font=('Arial', 15))
plat.menu.pack()


"""




plat.mainloop()
