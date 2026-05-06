import tkinter as tk 
from tkinter import messagebox
import os
from PIL import Image, ImageTk
students = []



def save_students():
    with open("students.txt", "w") as file:
        for i in range(students_listbox.size()):
            file.write(students_listbox.get(i) + "\n")

def load_students():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                students_listbox.insert(tk.END, line.strip())




def add_student():
    # students.append({"name": name, "age": age, "grade": grade})
    name = students_name_entry.get()
    age = students_age_entry.get()
    grade = students_grade_entry.get().upper()
    if name != "" and age != "" and grade != "" :
        students_listbox.insert(0, f"Name : {name}",
                                   f"Age  : {age} ",
                                   f"Grade :{grade}",
                                   f"──────────────────")
        added_label.config(text = f"  \n The Information You Add Are :\n Name : {name} \n Age : {age} \n Grade : {grade} ")
        name = students_name_entry.delete(0,tk.END)
        age = students_age_entry.delete(0,tk.END)
        grade = students_grade_entry.delete(0,tk.END)        
        messagebox.showinfo("Succee", "The Student Have Been Added")
        save_students()


    else:
        messagebox.showerror("Error", "There Is An Empty Field")
def show_student():
    # students.append({"name": name, "age": age, "grade": grade})
    students_listbox.config(text=f"Students Information : {students}.")

def delete_student():
    name = delete_student_entry.get()
    if name != "":
        for i in range(students_listbox.size()):
            if name in students_listbox.get(i):
                students_listbox.delete(i, i + 3)
                save_students()  # ← move it here, after deleting
                messagebox.showinfo("Success", "Student Deleted!")
                return
        messagebox.showerror("Error", "This Student Is Not On The List")
    else:
        messagebox.showerror("Error", "Please Enter A Student Name")


def show_login() :
    root.config(menu = "")
    home_screen.pack_forget()
    login_screen.pack()


def home():
    root.config(menu = home_menubar)
    login_screen.pack_forget()
    home_screen.pack()

def check_login():
    if user_name_entry.get() != "" and user_password_entry.get() != "":
        if  user_name_entry.get() == co_user_name and user_password_entry.get() == co_user_password :
            login_screen.pack_forget()
            user_name_entry.delete(0,tk.END)
            user_password_entry.delete(0,tk.END)

            home()
        else:
            messagebox.showerror("Error","User or Password is/are not correct")
    else:
        messagebox.showerror("Error","User or Password field is/are empty")

def show_add_student_page():
    student_info_page.pack_forget()
    home_screen.pack_forget()
    about_page.pack_forget()
    delete_student_page.pack_forget()
    add_students_page.pack()


def show_student_info_page():
    home_screen.pack_forget()
    add_students_page.pack_forget()
    about_page.pack_forget()
    delete_student_page.pack_forget()
    student_info_page.pack()

def about():
    about_label.config(text = "This Is A Student Page That Have \n All The Student Information You Entered.\n Powered By : \aOA")

def show_about():
    home_screen.pack_forget()
    add_students_page.pack_forget()
    student_info_page.pack_forget()
    about_page.pack()
    
def logout():
    root.config(menu="")
    home_screen.pack_forget()
    add_students_page.pack_forget()
    student_info_page.pack_forget()
    delete_student_page.pack_forget()
    about_page.pack_forget()
    login_screen.pack()
        


def show_delet_student_page():
    home_screen.pack_forget()
    add_students_page.pack_forget()
    student_info_page.pack_forget()
    about_page.pack_forget()
    login_screen.pack_forget()
    delete_student_page.pack()




    


co_user_name = "omer"
co_user_password = "1234"






root = tk.Tk() 
root.geometry("500x500")
root.title("Simple Student System")
root.iconbitmap(r"D:\Code\Python\Tkinter_Library\Photos\SSS1.ico")
root.resizable(False,False)


bg_image = Image.open(r"D:\Code\Python\Tkinter_Library\Photos\SSSbg.png")
bg_image = bg_image.resize((500, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



login_screen = tk.Frame(root)
# root.config(login_screen)


## user login Screen 

user_name_label = tk.Label(login_screen, text = "Enter Your User Name :")
user_name_label.pack()


user_name_entry = tk.Entry(login_screen)
user_name_entry.pack()


user_password_label = tk.Label(login_screen, text = "Enter Your User Password :")
user_password_label.pack()


user_password_entry = tk.Entry(login_screen, show="*")
user_password_entry.pack()



login_button = tk.Button(login_screen, text="Login", command = check_login)
login_button.pack()



## home Screen


home_screen = tk.Frame(root)




home_menubar = tk.Menu(root,tearoff = 0)


students_page = tk.Menu(home_menubar,tearoff = 0)
home_menubar.add_cascade(label= "Student_Page",menu = students_page)

about_menu = tk.Menu(home_menubar,tearoff=0)
home_menubar.add_cascade(label="About", menu = about_menu)


home_screen_label = tk.Label(home_screen,text = "Hi, Welcome to the Home Page")
home_screen_label.pack()






## add students page



add_students_page = tk.Frame(root)



add_student_page_menu_button = students_page.add_command(label="Add Student",command=show_add_student_page)

student_info_page = tk.Frame(root)

students_name_label = tk.Label(add_students_page, text="Enter The Name : ")
students_name_label.pack()



students_name_entry = tk.Entry(add_students_page)
students_name_entry.pack()


students_age_label = tk.Label(add_students_page, text="Enter The Age : ")
students_age_label.pack()


students_age_entry = tk.Entry(add_students_page)
students_age_entry.pack()

students_grade_label = tk.Label(add_students_page, text="Enter The Grade : ")
students_grade_label.pack()


students_grade_entry = tk.Entry(add_students_page)
students_grade_entry.pack()


students_button = tk.Button(add_students_page,text = "Add", command= add_student)
students_button.pack()

added_label = tk.Label(add_students_page, text = "")
added_label.pack()




## students info page



student_info_page_button = students_page.add_command(label="Show Students",command=show_student_info_page)

students_listbox = tk.Listbox(student_info_page, width=50, height=20)

## about page
about_page = tk.Frame(root)

about_label = tk.Label(about_page)
about_label.pack()

about_menu_button = about_menu.add_command(label = "About App", command=show_about)

about_show_button = tk.Button(about_page, text="Show",command=about)
about_show_button.pack()

login_screen.pack()



## delete student page
delete_student_page = tk.Frame(root)


delete_student_page_menu_button = students_page.add_command(label="Delete Student",command=show_delet_student_page)


delete_student_label = tk.Label(delete_student_page, text = "Enter The Student Name You Want To Delete :")
delete_student_label.pack()

delete_student_entry = tk.Entry(delete_student_page)
delete_student_entry.pack()

delete_student_button = tk.Button(delete_student_page, text = "Delete" , command = delete_student)
delete_student_button.pack()
## logout page

logout_menu_button = tk.Menu(home_menubar, tearoff=0)
logout_menu_button = students_page.add_command(label="Logout",command=logout)


students_listbox.pack()

load_students()
root.mainloop()

