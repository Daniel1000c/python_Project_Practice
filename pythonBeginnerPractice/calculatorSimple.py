"""
    TITLE: SIMPLE CALCULATOR
    
    7/20/24
    
    OBJECTIVE: Create a simple calculator that will perform addition, subtraction, multiplication, and division of two numbers
    
    Part 1:
        # Prompt user with the following menu options:
         1. Enter the first number
         2. Enter the second number
         3. Enter the operator(+,-,*,/)
    Part 2:
        # Print result of the numbers to the user in end statement
    Part 3: 
        # Prompt user if they want to do another calculation.
          1. if user enters yes then prompt user with two new numbers again
          2. if user enters no then end simple calculator.py
          
    Note: Create input invalidation if user inputs garbage or does calculation incorrectly
"""

# Print title for user to see
print("Simple Calculator Program")
print("-"*26)

# Create main function
def main():
    # Create while loop for menu options
    while True:
        try:
            # Prompt user for first number
            firstNumber = float(input("Enter the first number: "))
            
            # Prompt user for the second number
            secondNumber = float(input("Enter the second number: "))
        except ValueError:
            # Print input invalidation statement is prompt is string
            print("Invalid input, please try again")
            print()
            continue
        
        # Prompt user for the operator
        operator = input("Enter the operator(+,-,*,/): ")
        
        # Create if statement for each operator
        if operator == "+":
            # Create addition formula for user
            result = firstNumber + secondNumber
        elif operator == "-":
            # Create subtraction formula for user
            result = firstNumber - secondNumber
        elif operator == "*":
            # Create multiplication formula for user
            result = firstNumber * secondNumber
        elif operator == "/":
            # Create if statement is number is not divisible by 0 
            if secondNumber != 0:
                # Create division formula for user
                result = firstNumber / secondNumber
            else:
                # Print error statement that number is not divisible by 0
                print("Error: Number is not divisible by 0")
                continue
        else:
            # Print error message to user to use right operator
            print("Error: Invalid operator")
            print()
            continue
        
        # Print result to user
        print(f"Result:{round(result,1)}")
    
        # Prompt user if they want to do another calculation
        anotherCalc = input("Do you want to do another calculation? (yes/no): ")
        
        # Create if statement if user wants to continue or not.
        if anotherCalc != "yes":
            break
    
    # Print goodbye statement
    print("Goodbye!")
    
    
# Call main function
main()