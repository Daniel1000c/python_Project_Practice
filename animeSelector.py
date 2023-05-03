# Filename: animeSelector.py
# Description: Create a drive menu that prompts the user to:
#                       -1. Login
#                       -2. New User? Sign Up!
#                       -3. Developer Settings
#                       -4. Shutdown

# Input: userChoice

# Processing: 
#       1. Prompt user with drive menu
#           - Case 1: Login
#               * Log user into hub screen where user can pick anime title and genre of choice
#               * Prompt user for username and password
#               * Prompt user with drive menu:
#                   1. Choose an anime
#                       * Prompt user with genre of anime they would like
#                   2. Previously watched anime
#                       * Direct to a file list to show what anime they have watched in the past
#                   3. User Settings
#                       * Allow user to delete subscription from database, change username, change password
#                   4. Sign out
#                       * Bring user back to main menu
#           - Case 2: New User? Sign Up!
#               * Prompt new user with name, birthdate, username, and password
#               * Send personal info to file and record time and date of when user was created
#               * Redirect user back to main screen once done
#           - Case 3: Developer Settings
#               * Allow the developer to delete users form database as they see fit
#               * Show user how many people are logged into system 
#               * Allow developer to change font size and color of program
#           - Case 4: Shutdown: 
#               * Program will stop running and cease to boot up

# Output: Display anime selector menu to user

# Import datetime module to get accurate time of when user signed up
import datetime
# Import colorama module to decorate menu with color
import colorama
from colorama import Fore
colorama.init(autoreset = True)

# Create a class of menu choices for base drive menu
class baseMenuChoice:
    # Write chooses as strings in order to only accepts those inputs
    LOGIN = "1"
    NEW_USER = "2"
    DEVELOPER = "3"
    SHUTDOWN = "4"
    
# Create max attempts for main menu to log user out if attempts exceed max attempts
MAX_BASE_ATTEMPTS = 3

# Create function to center title header for each section
def createMenuHeader(menuHeader):
    # Create a newline to separate each header text from other menu options
    print()
    
    # Center header by 150 pixels
    baseMenuHeader =  menuHeader.center(150)  
    
    # Display section header
    print(baseMenuHeader) 
    
    # Create a newline for more separation between text
    print()
    
# Create placeholder menu choice for base menu
baseMenu = 0 

# Create main function to display base drive menu to user
def main():
    # Set counter for menu tries until user is locked out
    baseMenuTries = 0
    
    # Display base drive menu to user
    while baseMenu != baseMenuChoice.SHUTDOWN and baseMenuTries < MAX_BASE_ATTEMPTS:
        # Print title header for section
        createMenuHeader(menuHeader = Fore.CYAN + "\033[1;4mAnime Selector\033[0m")

        # Display menu options to user
        print(Fore.LIGHTCYAN_EX + "\t\t\t\t\t\t\tLogin.")
        print(Fore.LIGHTMAGENTA_EX + "\t\t\t\t\t\t\tNew User? Sign Up!")
        print(Fore.WHITE + "\t\t\t\t\t\t\tDeveloper Settings.")
        print(Fore.RED + "\t\t\t\t\t\t\tShutdown.")
        
        # Prompt user with base menu choice
        baseMenuOption = input("\tWhat Option Would You Like To Do? ")
        
        # Create branches for menu choice
        if baseMenuOption == baseMenuChoice.LOGIN:
            print("1")
            
            # Reset counter is user selects right option
            baseMenuTries = 0
            
        elif baseMenuOption == baseMenuChoice.NEW_USER:
            print("2")
            
            # Reset counter is user selects right option
            baseMenuTries = 0
            
        elif baseMenuOption == baseMenuChoice.DEVELOPER:
            print("3")
            
            # Reset counter is user selects right option
            baseMenuTries = 0
            
        elif baseMenuOption == baseMenuChoice.SHUTDOWN:
            print("Shutting Down ...")
            
            # Exit out of program once user is done with menu
            exit()
        else:
        # Display error message if user input is wrong
            print(Fore.RED + "Error ... Invalid Input. Must Be Options (1-4).")
            
            # Add one attempt to counter
            baseMenuTries += 1

    # lock user out of program if attempts match max attempts
    if baseMenuTries == MAX_BASE_ATTEMPTS:
        # Print out error message 
        print()
        print(Fore.BLUE + "\t\t\t\t\t\tToo Many Invalid Inputs... Try Again Later.")
main()

    