"""
  DATE: 7/15/2024
  
  TITLE: Simple ATM Program
  
  OBJECTIVE: Create a simple ATM program that will allow user to withdraw money from their account
  
  PART 1:
  * The user starts with a balance of $1000
  * Display following menu options to user:
    * Note: use  a while loop for this menu option
        1. Check Balance
            * Just use a print statement to reveal the balance to user
        2. Deposit Money  
            * new balance = current balance + deposit amount
        3. Withdraw Money
           * newbalance = current balance - withdraw amount
        4. Quit
           * Exit out of while loop and end program

  PART 2:
  * Create input validation for prompt if user inputs string or letters
  * Create an error message is user has no money in his account to withdraw money
  * Create an error message if user deposits negative amount of money.
"""

# Create title for atm program
print("Simple Chase Bank")
print("-"*18)
print("")

# Create main function
def main():
  # Create variable to store user input
  userInput = 0
  
  # Create variable to store user base account
  userBankAccount = 1000
  
  # Create while loop to keep program running until user wants to quit
  while userInput != 4:
    
    # Create menu list for user to choose from
    print("Choose One Of The Following Options: \n")
    print("\t1. Check Balance.")
    print("\t2. Deposit Money.")
    print("\t3. Withdraw Money.")
    print("\t4. Quit.")
  
    userInput = int(input("\nChoose an Option: "))
    
    if userInput == 1:
      # Create a print statement to reveal bank balance to user
      print(f"Your total balance is: ${userBankAccount}")
      
    elif userInput == 2:
      # Create a formula to add deposit amount to bank balance
      depositAmount = int(input("Enter the amount you want to deposit: "))
      userBankAccount = userBankAccount + depositAmount
      
    elif userInput == 3:
      # Create a subtraction formula to subtract withdraw amount from bank balance
      bankWithdraw = int(input("Enter the amount you want to withdraw: "))
      if bankWithdraw > userBankAccount:
        print("\nInsufficient funds. Please try again.")
        print()
      else:
        userBankAccount = userBankAccount - bankWithdraw
        
    elif userInput == 4:
      # Print goodbye message and exit program
      print("\nThank you and have a nice day.")
    else:
      # Print error message is user doesn't choose correct option
      print("Invalid option. Please try again.")
      print()
  
# Call main function
main()