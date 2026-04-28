

user = input("Enter Your User Name Here : ")
co_user = "omer"
if user == "":
    print("Empty Block")   
    exit()
elif user != "omer":
    print("please put the correct User Name") 
    exit()

password = input("Enter Your Password Here : ")
co_password ="1234"


if password == "":

    print("Empty Block")   
    exit()
elif password != "1234":
    print("please put the correct passowrd")
    exit()

if user == co_user and password == co_password :
    print("Next Page ....")