
# Numbers 
First_Num = float(input("Enter the first Number : "))
# op is a shortcut for opreations like (+, -, *, /)
Op = input("Enter the Op : ")
Second_Num = float(input("Enter the Second Number : "))
Result = My_Op()

#Conditions
def Zero_NagitveNum():
    
    if First_Num > 0 or Second_Num > 0 :
        print(f"The Result of this is : {Result}")
        return print("It can't do any op on nagtive numbers and 0")
#elif First_Num <= 0 or Second_Num <= 0:
        
    

#operations
def My_Op(First_Num, Second_Num):
    if Op == "+":
        return First_Num + Second_Num
    elif Op == "-" :
        return First_Num - Second_Num
    elif Op == "*":
        return First_Num * Second_Num
    elif Op == "/":
        return First_Num / Second_Num
    else:
        print("enter a valid op")
        return None



#Result = = 


