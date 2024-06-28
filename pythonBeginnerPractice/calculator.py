operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"total is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"total is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"total is {result}")
elif operator == "/":
    result = num1/num2
    print(f"total is {result}")
else:
    print(f"{operator} is a not a valid option")