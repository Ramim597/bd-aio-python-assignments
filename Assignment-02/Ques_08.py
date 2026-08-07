# Q8: Let's create a Simple Calculator that performs arithmetic operations.

# Create a function calculator(a, b, operation)
# that performs addition, subtraction,
# multiplication, or division based on
# the operation parameter.

# operation parameter can have values:
# '+', '-', '*' and '/'.


def calculator(a, b, operation):
    calc_val = 0
    if operation == "+":
        calc_val = a + b
    elif operation == "-":
        calc_val = a - b
    elif operation == "*":
        calc_val = a * b
    elif operation == "/":
        calc_val = a / b
    else:
        print("Invalid operation")

    print(calc_val)


num1 = int(input("Enter a number: "))
num2 = int(input("Enter anohter number: "))
operation = input("Enter operation (+, -, * and /.) any of them: ")
calculator(num1, num2, operation)
