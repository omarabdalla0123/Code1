# ---- input ----
def get_numbers():
    try: 
        a = float(input("Enter the First Number : "))
        b = float(input("Enter the Second Number : "))
        return a, b
    except ValueError : 
        print("Enter Numbers Only") 
        return None, None

# ---- Calculations ----

def get_op(a, b) :
    op = input("Enter the op you want : ")
    allowed_op = ["+","-","*","/"]

    if op not in allowed_op :
        print("Please enter on of ['+'','-'','*'','/''] ")
    elif op == "+" :
        return a + b
    elif op == "-" :
        return a - b
    elif op == "*" :
        return a * b
    elif op == "/" :
        return a / b
    else:
        return("No")

# ---- Main Program ----
try:
    first , second = get_numbers()
except ValueError:
    print("Empty places")
    exit()
result = get_op(first, second)

if first is not None and second is not None:
    print(result)
else:
    print("One or both palces is/are empyte/s")    

