# Get user input for two numbers and the operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if the user is trying to divide by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operation."

# Display the result
print(f"{num1} {operation} {num2} = {result}")
