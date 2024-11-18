# Function to perform the chosen operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# Collecting user input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Performing the calculation
result = calculate(number1, number2, operation)

# Displaying the result
print(f"{number1} {operation} {number2} = {result}")
