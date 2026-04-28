

def add(a,b) :
    return  a + b

def subtract(a,b):
    return a - b
try :
    first_number = int(input("Enter  First Number : "))

    second_number = int(input("Enter  Second Number : "))
except ValueError :
    print("Numbers only")
    exit()

operation = input("Choose operation (+, -) : ")



if operation == "+":
    result= add(first_number, second_number)
elif operation == "-" :
    result= subtract(first_number, second_number)
else :
    print("Choose (+, -) only.")    
    exit()

print(f"Result : {result}")