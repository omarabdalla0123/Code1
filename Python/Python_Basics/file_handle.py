

user = ""

while True :
    user = input("Choose (a=add, s=show, q=quit) : ").lower()

    if user == "a" :
        user = input("What you want to add : ")
        with open("f1.txt", "a" ) as file :
            file.write(user)
    elif user == "s" :
        with open("f1.txt", "r") as file:
            note = file.read()
            print(f"this is your notes {note}")
    elif user == "q" :
        print("see you later")
        exit()