# ---- Inputs ----
student_name = input("Enter The Student Name : ")
marks = int(input("Enter The Student Marks : "))


# ---- Conditions ----

if marks > 90 :
    print("Your Grad is 'A'")
elif 90 < marks > 70 :
    print ("Your Grad is 'B'")
elif 70 < marks > 50 :
    print("Your Grad is 'C'")
elif marks < 50 :
    print("Your Grad is 'F'")    