#Calculator

#----input----

def get_numbers():
   try: 
    first_number = float(input("Enter The First Number : "))

    second_number = float(input("Enter The Second Number : "))
    return first_number , second_number
   except ValueError:
       print(" Put Numbers Only ")
       return None, None    
     
   

def get_op():
  
    op = input("Enter The Op : ").strip()
    allowed_op = ["+","-","*","/"]   
       
    if len(op) != 1 :
       print("Chose the op one time only")
    elif op not in allowed_op :
        print("Put One of '+,*,-,/'")
        return None
    return op
# ----Calculation ----


def calculation(a, b, op):    
    if a is None or b is None:
        print("Invalid input - please enter valid numbers")
        return None
    
    if a <= 0 or b <= 0:
        print("It Only Calculate Numbers Bigger Than 0")
        return None
      
    if op == "+" :
        return a + b
    elif op == "*" :
        return a * b    
    elif op == "-" :
        return a - b
    elif op == "/" :
      if b == 0:
         print("You cannot divide by zero.")
         return None
    return a / b 


 # ---Main Program      
first_number , second_number = get_numbers() 
if first_number is None or second_number is None :
    exit()    

op = get_op() 
if op is None:
      exit()          
        
result = calculation(first_number, second_number, op)
if result is not None :
    print(f"The result is : {result}")    
        