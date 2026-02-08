from tkinter import *
# It finished , but there is more impovement i can do.
def User_Password():


    def clear_button() :
        user.delete(0,END)
        password.delete(0,END)

    root = Tk()

    # Main option for tk :-
    root.title("User & Password")
    root.geometry("1000x1000")
    root.resizable(False,False)

    # Entry Displays :-

    user = Entry(root, font=('Arial', 20))
    user.grid(row=0, column=1)

    password = Entry(root, font=('Arial',20), show='*')
    password.grid(row=1, column=1)



    #Lebals :-

    user_label = Label(root, font=('Arial', 20), text="User Name")
    user_label.grid(row=0, column=0)

    password_label = Label(root, font=('Arial', 20), text="Password ")
    password_label.grid(row=1, column=0)
   #Buttons:-

    enter = Button(root, text="Enter",font=('Arial',18))
    enter.grid(row=2, column=1, )

    clear = Button(root, text="Clear", font= ('Arial',18), command = clear_button)
    clear.grid(row=0, columns=5)

    root.mainloop()



User_Password()