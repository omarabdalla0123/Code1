# ---- File Manger ----#
# tkinter part


import os 

os.rename('d:/Code/Python_Projects/Real_Work/Tkinter_Part.py','d:/Code/Python_Projects/Real_Work/File_Manger/Tkinter_Part.py')

print(os.getcwd())

import tkinter as tk

root = tk.Tk()

root.title('File Orgnaizer')
root.geometry("500x500")
root.resizable(False,False)

main_button = tk.Button(root, text = 'Main Button')
main_button.place(relx=0.5, rely=0.5, anchor='center')
root.mainloop()


