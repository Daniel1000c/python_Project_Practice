"""
 Date: 7/11/24
 
 Objective: Create a simple arithmetic program that will perform addition, subtraction, multiplication, and division of two numbers
 
 Goal: Create a simple arithmetic program
 
 Part 1:
  *Prompt user for the first number
  *Prompt user for the second number
  
 Part 2:
  *Add the two numbers
  *Subtract the two numbers
  *Multiply the two numbers
  *Divide the two numbers
  
 Part 3:
 * Create input invalidation for prompt   
"""

# Print title out for user to see
print("Simple Arithmetic Program")
print("-"*25)

# Create main function
def main():
    # Prompt user for first number
    firstNumber = float(input("Enter the first number: "))

    # Prompt user for the second number
    secondNumber = float(input("Enter the second number: "))
    
    # Prompt user if they would like to add, subtract, multiply, or divide
    userOperation = str(input("Enter your operator (+, -, *, /): "))

   # Create if statement for operators
    if userOperation == "+" or userOperation == "add":
        # Create formula for addition
        sum = firstNumber + secondNumber
        print(f"The sum of the two number is: {sum}")
    elif userOperation == "-" or userOperation == "subtract":
        # Create formula for  Subtraction
        subtract = firstNumber - secondNumber
        print(f"The subtract of the two number is: {subtract}")
    elif userOperation == "*" or userOperation == "multiply":
        # Create formula for  Multiplication
        multiplication = firstNumber * secondNumber
        print(f"The multiplication of the two number is: {multiplication}")
    elif userOperation == "/" or userOperation == "divide":
        # Create formula for Division 
        division = firstNumber / secondNumber
        print(f"The division of the two number is: {division}")
    else:
        # Create input invalidation if prompt is garbage input
        print("Invalid input, please try again")


# Call main function that houses rest of code
main()