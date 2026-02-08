# This is a longer Python script that includes a runtime error: ZeroDivisionError
# It simulates a simple calculator that divides two numbers, but allows division by zero

def divide_numbers(a, b):
    """Function to divide two numbers."""
    return a / b

# Main program
print("Welcome to the Simple Divider!")
print("This program divides two numbers.")

# Get user input (but we'll hardcode for the error)
num1 = 10
num2 = 0  # This will cause the error

print(f"Dividing {num1} by {num2}...")

try:
    result = divide_numbers(num1, num2)
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    # Note: Even though we catch it, the error still occurs; remove the try-except to see the raw error

# Additional code that runs after (but won't if error is unhandled)
print("Program finished.")
