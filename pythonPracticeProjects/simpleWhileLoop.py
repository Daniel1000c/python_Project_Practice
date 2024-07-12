"""
    Date: 7/12/24
    
    objective: Create a simple while loop program that will keep going until the user inputs 0
    
    Step one:
        * Create a while loop for a condition that will keep going until user input equals 0 
        * Ask user for a number
        * Keep asking user for another number.
        * If user inputs 0 then add all numbers from previous inputs and output the total
    
    Step Two: 
      * Create input validation for prompt if user inputs string or letters
"""


# Create title for while loop program 
print("Simple While Loop Program")
print("-"*25)

# Create main function
def main():
    # Create a 
    # total counter for each number and set it to 0
    total = 0
    # Create input invalidation for prompt if user inputs string or letters
    while True:
        try:
            # Prompt user for a number
            userPrompt = int(input("Enter a number: "))
            
            if userPrompt == 0:
                break
            
            # add number total 
            total += userPrompt
            
        except ValueError:
            print("Invalid input, please try again")
    
    # Print total to output terminal if user inputs 0
    print(f"The total is {total}")
    

# Call main function
main()
        