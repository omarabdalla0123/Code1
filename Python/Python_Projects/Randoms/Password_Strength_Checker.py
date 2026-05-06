# ---- inputs ----
correct_password = '1234'
check_box = ""



# ---- Loops & If Conditions ----


while check_box != correct_password :
    check_box = input("Enter The Password : ")



if check_box == correct_password :
    print("You Won")
else :
    print("It Is Wrong Passowrd" + "\n try again")