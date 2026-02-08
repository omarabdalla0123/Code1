def calculator():
    print("Simple calculator")
first_number = int(input("Enter the First Number here : "))
operator = input("Enter operator (+,-,*,/): ")
second_number = int(input("Enter the Second Number here : "))
if operator =='+':
    result = first_number + second_number
    print(f"{first_number} { operator } {second_number} = {result}")
elif operator =='-':
    result = first_number - second_number
    print(f"{first_number} { operator } {second_number} = {result}")
elif operator =='*':
    result = first_number * second_number
    print(f"{first_number} { operator } {second_number} = {result}")

elif operator =='/':
    result = first_number / second_number
    print(f"{first_number} { operator } {second_number} = {result}")
