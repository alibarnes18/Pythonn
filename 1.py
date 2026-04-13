num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("enter the operation you want to perform (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)

elif operation == "-" :
    print(num1 - num2)
elif operation == "*" :
    print(num1 * num2)      
elif operation == "/" :
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")