""" Scenario: Create a system that takes track of staff attendance at a local hospital when ever they sign in to work. The program should be able to:
    1. Take employee attendance and send it to a file for database
        * Create password for employee login
        * keep track employee passwords in a database to check for input invalidation
        * lock user out of system if menu options if not equal to correct choice
    2. Mark calendar for when employees are off 
        * Highlight days for employees with colors like red or green to tell if a employee reported to work or not
        * Keep track of how many hours the employees worked during those days
        * Show the name of the employee that worked that day.
    3. Announce when there will be days off and employee bonuses.
        * one of the menu options will display certain days on which there will be bonuses and also showing when workers can take a day off 
"""
# Constants & Variables
PASS_MENU_PROMPT_TRIES = 3
MAX_MENU_TRIES = 4
TAKE_ATTENDANCE = "1"
MARK_CALENDER = "2"
EXTRACURRICULARS = "3"
QUIT_MENU = "4"

# Import getpass module to hide user passwords
from getpass import getpass

# Import colorama module to change error texts to red to show error clearly
import colorama
from colorama import Fore
colorama.init(autoreset = True)

# Create function to format title header for each section
def createTitleHeader(tabHeader):
    # Center header by 70 pixels
    centerHeader = tabHeader.center(100)

    # Convert header into a f string and underline for header sections
    print(centerHeader)

    # Create a whitespace for title header to organize better
    print()
    
# Create employee login homepage
def createHomePage():
    print("\nHello world")
    
# Create function for employee login
def employeeLogin():
    # Insert header function for tab section
    createTitleHeader(tabHeader = "\033[1;4mEmployee Attendance\033[0m")
    
    # Create a counter for menu tries
    passwordMenuPromptTry = 0
    
    # Create empty list for employee usernames and password
    loginDatabase = []
    
    # Create while loop to return user to prompt screen to login as new user
    while True and passwordMenuPromptTry < PASS_MENU_PROMPT_TRIES:
        # Prompt user to see if they are registered user or not
        employeeLoginCheckpoint = str(input("Are you Already Registered To This Hospital (Yes/No) Or Enter M To Go To Main Screen: "))
        
        # Create input invalidation for password prompt menu
        if employeeLoginCheckpoint == "No" and employeeLoginCheckpoint == "Yes" and employeeLoginCheckpoint == "M":
            passwordMenuPromptTry = 0

        if employeeLoginCheckpoint == "No":
            print()
            createTitleHeader(tabHeader = "Employee Register Information")

        # Prompt user for employee name, Id, birthday, occupation
            registerName = str(input("Please Enter Employee Name: "))
            registerBirthday = str(input("Please Enter Birthday: "))
            jobTitle = str(input("Please Enter Job Title: "))
            print()
        
        # Write employee personal info to a file
            fileObject = open("employeeInfoDatabase.txt","a")

        # Add items to file after information is inputed
        # Create newline to separate multiple pieces of employee info
            NEWLINE = "\n"
            fileObject.write(str(registerName))
            fileObject.write('          ')
            fileObject.write(str(registerBirthday))
            fileObject.write('          ')
            fileObject.write(str(jobTitle))
            fileObject.write(NEWLINE)
        
        # Close file 
            fileObject.close()

        # Prompt user for new password and username
            createUsername = str(input("Please Create New Username: "))
            createPassword = str(input("Please Create New Password: "))
            registerWorkerId = str(input("Please Enter Worker Id: "))
            print()
            
        # Append username, password, and worker id to empty list
            loginDatabase.append(createUsername)
            loginDatabase.append(createPassword)
            loginDatabase.append(registerWorkerId)
            loginDatabase.append(NEWLINE)

        elif employeeLoginCheckpoint == "Yes":
            createTitleHeader(tabHeader = "\033[1;4mEmployee Login\033[0m")
            print()
            
            # Prompt user for username, password, and employee id number
            employeeUsername = str(input("\nPlease Enter Username: "))
            
            if employeeUsername == createUsername and createUsername in loginDatabase:
                # Prompt user for password once username is correct
                employeePassword = getpass("\nPlease Enter Password: ")
                
                if employeePassword == createPassword and createPassword in loginDatabase:
                    # Prompt user for worker id once password is correct
                    workerId = str(input("\nPlease Enter Worker Id: "))
                    
                else:
                    # Print error message if password is not correct
                    print(Fore.RED + "Error ... Password Does Not Exist")
                    print()
                    
                    # Bring user to login home page after user enters correct worker id
                    if workerId == registerWorkerId and registerWorkerId in loginDatabase:
                        createHomePage()# needs attention
                    else:
                            print(Fore.RED + "Error ... Worker Id Does Not Exist!!!")# needs attention
            else:
                #print error message if username is not correct
                print(Fore.RED + "Error ... Username Does Not Exist!!!!")

        elif employeeLoginCheckpoint == "M":
        # Call main function to return user back to main menu
            print()
            main()
        
        else:
            print(Fore.RED + "Error ... Invalid Input!!! Has To be Either Yes, No, or M.")
            passwordMenuPromptTry +=1
        
        # Lock user from entering more input after try limit and revert user back to main menu
        if passwordMenuPromptTry == PASS_MENU_PROMPT_TRIES:
            # Create error message for user and revert user back to menu
            print()
            print(Fore.RED + "Error ... Invalid Number Of Inputs")
            print()
            main()

# Create function to house main body of program
def main():
# Set menu option for drive menu to zero
    drive_menu_option = 0

# Create intro
    createTitleHeader(tabHeader = "\033[1;4mMemorial Hospital Employee Login\033[0m")

# Create drive menu
# Create limit counter for amount of tries user has to type
    driveMenuTries = 0  
    while drive_menu_option != QUIT_MENU and driveMenuTries < MAX_MENU_TRIES:
        # Create options for menu
        print("\nChoose One Of The Following Options:")
        print("\t1. Take Employee Attendance.")
        print("\t2. Mark Worker Calendar.")
        print("\t3. Employee Bonuses And News.")
        print("\t4. Log Off.")
        drive_menu_option = input("Please Choose An Option: ")

        # Create input invalidation if user provides bad input
        if drive_menu_option >= TAKE_ATTENDANCE and drive_menu_option <= QUIT_MENU:
            # Resets tries counter if user does provide good input
            driveMenuTries = 0

        # Create tabs for menu choices
        if drive_menu_option == TAKE_ATTENDANCE:
           employeeLogin()
        elif drive_menu_option == MARK_CALENDER:
            print()
        elif drive_menu_option == EXTRACURRICULARS:
            print()
        elif drive_menu_option == QUIT_MENU:
            # Creating good bye message when user is done with program
            print("Logging Off. Good Bye")
            print()
            
            # Exit out the loop to end program
            exit()
        else:
            print(Fore.RED + "Error ... User Input Is Incorrect!!! Choose Options (1-4).") 
            print()
            driveMenuTries += 1
    
        # Create error message for user if they put too many bad inputs
    if driveMenuTries == MAX_MENU_TRIES:
        print(Fore.RED + "Error!!!! User Did Too Many Bad Input. Too Many Bad Inputs.")

main()