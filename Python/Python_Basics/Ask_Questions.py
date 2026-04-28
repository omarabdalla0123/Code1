
score = 0

first_q =input("Ener you name : ")

if first_q != "":
    print(f"Hi {first_q}")
    print("+ 1 point. added to score")
    score = 1 + score

second_q = int(input("Enter your age : "))
if second_q != "" :
    print("+ 1 point. added to score")
    score = 1 + int(score) 


if second_q < 20 :
    print(" you are not allowed. (you are under 20)")
    print(score)
    exit()
elif second_q > 50 :
    print("you are not allowed. (you are older than 50)")
    print(score)
    exit()
else :
    print("you are allowed. your age is between 20 - 49")




third_q = input("if you studing click on (s), if you have a job click on (j) : ")

if third_q == "s" :
    third_q = "student"
    print("so you are a student")
    print("+ 1 point. added to score")
    score = 1 + int(score)
elif third_q =="j":
    third_q = "emoployee/r"
    print("so you are an emoployee/r")
    print("+ 1 point. added to score")
    score = 1 + int(score)
else :
    print("Please just click on  (s) or (j)")   

fourst_q = input("if you have an apartment  click on (a), if you have a house click on (h) : ")


if fourst_q == "a" :
    fourst_q = "Apartment"
    print("you have apartment")
    print("+ 1 point. added to score")
    score = 1 + int(score)
elif fourst_q =="h":
    fourst_q = "House"
    print("you have a house ")
    print("+ 1 point. added to score")
    score = 1 + int(score)
else :
    print("Please just click on  (a) or (h)")        

print(f"You are {first_q}, you are a {second_q} years old, and you are a/an {third_q}, also you are living in {fourst_q}. \n Your Score is {score} Points. ")


